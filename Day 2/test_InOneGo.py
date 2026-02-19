from SighnupZipangApp_PageObject import *
import time
import os
class Test_All_Testcases:

    def test_Login_workflow(self, driver):

        pl = ZipangLogin(driver)

        time.sleep(2)
        pl.set_previewButton()

        time.sleep(2)
        pl.set_Select_all_button()

        time.sleep(2)
        pl.set_Bid_icon()

        time.sleep(3)
        pl.set_Increase_button()

        time.sleep(3)
        pl.set_Place_button()
        pl.set_Grid_view_button()

        driver.get_screenshot_as_file(
            r"D:\Aarav\Selenium\Day 2\Screenshots\Screenshots1.png"
        )

        pl.set_PageChanger()
        pl.set_Enter_amount_text("123546")
        pl.set_Press_yes_button()

        time.sleep(1)

        driver.get_screenshot_as_file(
            r"D:\Aarav\Selenium\Day 2\Screenshots\Screenshots2.png"
        )

    def test_Bulk_WithoutSelection(self,driver):
        pl = ZipangLogin(driver)
        pl.set_previewButton()

        bb = ZipangBulkBid(driver)
        time.sleep(2)
        bb.set_BulkBidButton_xpath_WithoutSelection()

    def test_Bulk_WithSelection(self,driver):
        pl = ZipangLogin(driver)
        pl.set_previewButton()

        bb = ZipangBulkBid(driver)
        time.sleep(2)
        bb.set_BulkBidButton_xpath_WithSelection()

    def test_Download(self,driver):
        pl = ZipangLogin(driver)
        pl.set_previewButton()

        dd = ZipangDownload(driver)
        time.sleep(2)
        dd.set_Download_option()
        time.sleep(5)
        files = os.listdir(r"D:\Aarav\Selenium\Day 2\Downloads")

        assert len(files) > 0

    def test_Favorite(self,driver):
        pl = ZipangLogin(driver)
        pl.set_previewButton()

        fa = ZipangFav(driver)
        time.sleep(3)
        fa.set_favoriteButton()

    def test_NR_ClickAndVerify(self,driver):
        pl = ZipangLogin(driver)
        pl.set_previewButton()

        nr = ZipangNR(driver)
        nr.set_Prev_button()
        nr.set_NR_button()
        time.sleep(4)
        nr.set_NR_present()

    def test_NR_VerifyWithoutClick(self,driver):
        pl = ZipangLogin(driver)
        pl.set_previewButton()

        nr = ZipangNR(driver)
        After_Click = nr.set_NR_displayed_after()
        Before_click = nr.set_NR_displayed_before()

        assert After_Click != Before_click

    def test_PlaceBid_WithoutAmount(self,driver):
        pl = ZipangLogin(driver)
        pl.set_previewButton()

        pb = ZipangPlaceBid(driver)
        pb.Next_page_button()
        time.sleep(2)
        pb.set_placeBid_xpath_empty()

    def test_placeBid_EnterValidAmount(self,driver):
        pl = ZipangLogin(driver)
        pl.set_previewButton()

        pb = ZipangPlaceBid(driver)
        time.sleep(2)
        pb.set_placeBid_xpath_ValidAmount()

    def test_placeBid_EnteNegativeAmount(self,driver):
        pl = ZipangLogin(driver)
        pl.set_previewButton()

        pb = ZipangPlaceBid(driver)
        time.sleep(2)
        pb.set_placeBid_xpath_Negativeamount()

    def test_Search_Empty(self,driver):
        pl = ZipangLogin(driver)
        pl.set_previewButton()

        sa = ZipangSearch(driver)
        time.sleep(3)
        sa.set_SearchButton("")
        sa.is_result_present()

    def test_Search_ValidResult(self,driver):
        pl = ZipangLogin(driver)
        pl.set_previewButton()

        sa = ZipangSearch(driver)
        sa.set_SearchButton("1")
        sa.set_Search_Valid()

    def test_Search_TnvalidResult(self,driver):
        pl = ZipangLogin(driver)
        pl.set_previewButton()

        sa = ZipangSearch(driver)
        sa.set_SearchButton("Aarav")
        sa.set_Search_Valid()