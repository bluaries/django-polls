import datetime

from django.utils import timezone
from django.contrib.auth.models import User
from django.test import LiveServerTestCase
from selenium import webdriver

from polls.models import Question, Choice

def create_question(question_text, days):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class SeleniumFunctionalTests(LiveServerTestCase):
    username = "testuser"
    password = "password"

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver_win32/chromedriver.exe")
        super(SeleniumFunctionalTests, self).setUp()
    
    def tearDown(self):
        self.browser.quit()
        super(SeleniumFunctionalTests, self).tearDown()

    def test_find_h1_tag(self):
        self.browser.get(self.live_server_url + "/polls")
        elements_tag = self.browser.find_element_by_tag_name("h1")
        self.assertEqual("Polls for you!", elements_tag.text)

    def test_find_polls(self):
        test_quest = create_question("Test-Question", days=0)
        self.browser.get(self.live_server_url + "/polls")
        quest = self.browser.find_element_by_id(f"quest-{{test_quest.id}}")
        self.assertEqual("Test-Question", quest.text)

    def test_hyperlink(self):
        test_quest = create_question("Test-Question", days=0)
        self.browser.get(self.live_server_url + "/polls")
        hyperlink = self.browser.find_elements_by_tag_name("a")
        hyperlink[0].click()
        self.assertEqual(self.browser.current_url, self.live_server_url + "/polls/" + f"{test_quest.id}/")

        

        