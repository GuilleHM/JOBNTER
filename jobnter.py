'''
This script automatically logs into LinkedIn website using "username" and "password" fields.
Then, finds jobs that match the "position" and "location" criteria and has an "Easy Apply"
button, ordered by descending chronological order.
Afterwards, it iterates over those jobs and submits applicant´s CV to those jobs, up to a
predefined MAX. number of applications.
The script assumes that job submission form fields (e-mail and phone number) are populated by
cookies already installed on user´s computer. Likewise, CV should be attached automatically by
LinkedIn. These requirements are easily met once applicant has already submitted at least one
job submission form manually.
Before running it, you need to fill in input parameters (username, password, position and location)
with you own data.
'''


# Importing needed modules and classes
import sys, time, random, os, csv, datetime, pyautogui
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


def main():
    # Defining logging and search parameters
    username = 'XXXXXX'
    password = 'XXXXXX'
    position = 'XXXXXX'
    location = 'XXXXXX'

    # Getting a list of already applied jobs
    filename = 'alreadyappliedjoblist.csv'
    try:
        df = pd.read_csv(filename, header=None)
        appliedJobIDs = list(df.iloc[:, 1])
    except:
        appliedJobIDs = []

    # Starting the bot
    bot = EasyApplyBot(username, password, position, location, appliedJobIDs, filename)
    bot.start_apply()


class EasyApplyBot:
    # Parameter to limit the number of job applications to be sent
    MAX_APPLICATIONS = 100

    def __init__(self, username, password, position, location, appliedJobIDs, filename):
        # Using Chrome as automatic browser
        chromepath = os.getcwd() + '\\chromedriver.exe'
        self.options = self.browser_options()
        self.browser = webdriver.Chrome(options=self.options, executable_path=chromepath)
        # Defining internal parameters
        self.position = position
        self.location = location
        self.appliedJobIDs = appliedJobIDs
        self.filename = filename
        # Logging into LinkedIn
        self.start_linkedin(username, password)

    def browser_options(self):
        # Browser initialization options
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--ignore-certificate-errors")
        # options.add_argument('--headless') # to be enabled when script is tested.
        options.add_argument('--no-sandbox')
        options.add_argument("--disable-extensions")
        return options

    def start_linkedin(self, username, password):
        self.browser.get("https://www.linkedin.com/login?trk=guest_homepage-basic_nav-header-signin")
        try:
            time.sleep(2)
            user_field = self.browser.find_element_by_id("username")
            pw_field = self.browser.find_element_by_id("password")
            login_button = self.browser.find_element_by_css_selector(".btn__primary--large")
            user_field.send_keys(username)
            user_field.send_keys(Keys.TAB)
            time.sleep(1)
            pw_field.send_keys(password)
            time.sleep(1)
            login_button.click()
            time.sleep(1)
        except:
            print("It hasn't been possible to logging. Please, check possible causes.")
            sys.exit(1)
            
    def start_apply(self):
        count_application = 0
        count_job = 0
        start_at_job = 0

        while count_application < self.MAX_APPLICATIONS:
            self.browser, _ = self.next_jobs_page(start_at_job)
            # Sleeping to make sure everything loads. Adding randomness to make us look human.
            time.sleep(random.uniform(3.5, 6.9))
            # Getting job links
            links = self.browser.find_elements_by_xpath('//div[@data-job-id]')
            # Getting job ID of each job link
            IDs = []
            for link in links:
                temp = link.get_attribute("data-job-id")
                jobID = temp.split(":")[-1]
                IDs.append(int(jobID))
            if len(IDs) == 0:
                print("No jobs to apply. Please, check.")
                break
            IDs = set(IDs)
            # Removing already applied jobs
            jobIDs = [x for x in IDs if x not in self.appliedJobIDs]
            # If already applied to all jobs on this page, go to the next one.
            if len(jobIDs) == 0:
                self.avoid_lock()
                start_at_job = start_at_job + 25
                count_job = 0
                continue
            # Looping over IDs to apply
            for jobID in jobIDs:
                count_job += 1
                self.get_job_page(jobID)
                # Getting "easy apply" button
                button = self.get_easy_apply_button()
                if button is not False:
                    string_easy = "Has 'Easy Apply' Button"
                    button.click()
                    success = self.send_resume()
                    if success:
                        count_application += 1
                else:
                    string_easy = "Doesn't have 'Easy Apply' Button"
                    success = True
                # Appending applied job ID to 'alreadyappliedjoblist.csv' file
                timestamp = datetime.datetime.now()
                toWrite = [timestamp, jobID, string_easy]
                toWrite2 = [timestamp, jobID, 'Impossible to apply']
                with open(self.filename, 'a', newline='') as f:
                    writer = csv.writer(f)
                    if success:
                        writer.writerow(toWrite)
                    else:
                        writer.writerow(toWrite2)
                # Exiting the loop if MAX_APPLICATION reached (this option is for having the
                # option to exit the application within first job page search along script
                # testing stage.
                if count_application == self.MAX_APPLICATIONS:
                    print("Max number of applications reached.")
                    sys.exit(0)
                # Sleeping every 20 applications
                if count_application != 0 and count_application % 20 == 0:
                    sleepTime = random.randint(300, 600)
                    print('\n\n****************************************\n\n')
                    print('Time for a nap - see you in: ' + str(int(sleepTime / 60)) + 'min...')
                    print('\n\n****************************************\n\n')
                    time.sleep(sleepTime)
                # Going to a new page if all jobs are done
                if count_job == len(jobIDs):
                    self.avoid_lock()
                    start_at_job = start_at_job + 25
                    count_job = 0

        self.finish_apply()

    def next_jobs_page(self, start_at_job):
        self.browser.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&keywords=" +
                         self.position + "&location=" + self.location + "&sortBy=DD&start=" +
                         str(start_at_job))
        self.avoid_lock()
        self.load_page()
        return (self.browser, start_at_job)

    def avoid_lock(self):
        x, _ = pyautogui.position()
        pyautogui.moveTo(x + 200, None, duration=1.0)
        pyautogui.moveTo(x, None, duration=0.5)
        pyautogui.keyDown('ctrl')
        pyautogui.press('esc')
        pyautogui.keyUp('ctrl')
        time.sleep(0.5)
        pyautogui.press('esc')

    def load_page(self, sleep=1):
        if sleep == 1:  # for job search pages (25 jobs per page)
            time.sleep(sleep)
            self.browser.find_element_by_class_name('jobs-search-results').send_keys(Keys.END)
        else:  # for specific jobs pages
            time.sleep(sleep * 3)
            # Adding some human-like behavior
            scroll_page = 0
            while scroll_page < random.randint(1200, 2400):
                self.browser.execute_script("window.scrollTo(0," + str(scroll_page) + " );")
                scroll_page += 200
            time.sleep(sleep * 3)
            self.browser.execute_script("window.scrollTo(0,0);")
        page = BeautifulSoup(self.browser.page_source, "lxml")
        return page

    def get_job_page(self, jobID):
        job = 'https://www.linkedin.com/jobs/view/' + str(jobID)
        self.browser.get(job)
        time.sleep(1)
        self.job_page = self.load_page(sleep=0.5)
        return self.job_page

    def get_easy_apply_button(self):
        try:
            EasyApplyButton = self.browser.find_element_by_class_name("jobs-apply-button")
        except:
            EasyApplyButton = False
        return EasyApplyButton

    def send_resume(self):
        try:
            # Click checkbox for not following the company
            chbox = self.browser.find_element_by_class_name("jobs-apply-form__follow-company-label")
            chbox.click()
            # Submit CV (assumes e-mail and telephone fields already populated by cookies)
            submit_button = self.browser.find_element_by_class_name("jobs-apply-form__submit-button")
            submit_button.click()
            success = True
            time.sleep(random.uniform(3, 5))
        except:
            # In case this position is one of those that opens a new tab in order to collect
            # more data for recruiting process, we just close the tab without applying to it.
            success = False
            time.sleep(random.uniform(3, 5))
            if self.browser.window_handles[1]:
                self.browser.switch_to.window(self.browser.window_handles[1])
                self.browser.close()
                self.browser.switch_to.window(self.browser.window_handles[0])
            time.sleep(random.uniform(3, 5))
        finally:
            return success

    def finish_apply(self):
        self.browser.close()


if __name__ == '__main__':
    main()
