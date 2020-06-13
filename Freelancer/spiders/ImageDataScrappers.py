import scrapy
from ..items import FreelancerItem
import mysql.connector


class ScrapeHotel(scrapy.Spider):
    name = 'images'
    # start_urls = [
    #     'https://www.apartments.com/union-chapel-hill-chapel-hill-nc/q9gsgqy/'
    # ]

    def __init__(self, *args, **kwargs):
        urls = kwargs.pop('urls', [])
        if urls:
            print("****************************************************")
            print(urls)
            print("****************************************************")
            self.start_urls = urls.split(',')
        self.logger.info(self.start_urls)
        super(ScrapeHotel, self).__init__(*args, **kwargs)

    def parse(self, response):
        items = FreelancerItem()

        my_url_starting = response.request.url

        mydb = mysql.connector.connect(host="zrd.hrz.mybluehost.me", user="zrdhrzmy_star", passwd="safd$#SDF43",
                                       database="zrdhrzmy_MLSData")
        cursor = mydb.cursor()
        sql_select_Query = 'SELECT task_uid FROM zrdhrzmy_MLSData.task_queue where url = "' + str(my_url_starting) + '"'
        cursor.execute(sql_select_Query)
        my_task_id_from_database = cursor.fetchall()
        cursor.close()
        mydb.close()

        print("*************************")
        print("THe Unique Id is :",my_task_id_from_database)
        print("****************************")


        mydb = mysql.connector.connect(host="zrd.hrz.mybluehost.me", user="zrdhrzmy_star", passwd="safd$#SDF43",
                                       database="zrdhrzmy_MLSData")
        cursor = mydb.cursor()

        PropIdMLS_query = 'SELECT PropIdMLS FROM zrdhrzmy_MLSData.property_mls_data where task_uid = "' + str(my_task_id_from_database[0][0]) + '"'
        cursor.execute(PropIdMLS_query)
        PropIdMLS_query_answer = cursor.fetchall()





        IdMLS_query = 'select * from zrdhrzmy_MLSData.image_mls_data order by id DESC LIMIT 1;'
        cursor.execute(IdMLS_query)
        IdMLS_query_answer = cursor.fetchall()
        if len(IdMLS_query_answer) !=0:
            IdMLS_query_answer = IdMLS_query_answer[0][0] + 1
        else:
            IdMLS_query_answer = 1


        print("*************************")
        print("THe Sequential Property id  is :",IdMLS_query_answer)
        print("****************************")



        cursor.close()
        mydb.close()

        my_task_id_from_database = my_task_id_from_database[0][0]
        print(PropIdMLS_query_answer)

        PropIdMLS = PropIdMLS_query_answer[0][0]
        items['task_uid'] = my_task_id_from_database

        image_block = response.css("#gallery0")
        imageCode = image_block.css(".item ul li")
        print(type(imageCode))
        i=1
        for images_single in imageCode:
            ImageNumberMLS=images_single.css(".galleryItemImage::attr(data-attachmentid)").get()
            ImageTypeMLS= images_single.css(".galleryItemImage::attr(data-attachmenttypeid)").get()
            ImageTypeMLS = ImageTypeMLS.replace(";","")
            ImageUrlMLS = images_single.css(".galleryItemImage::attr(data-image)").get()
            ImageAltMLS = images_single.css(".galleryItemImage meta::attr(title)").get()
            print("************************")
            print(i,ImageNumberMLS,ImageTypeMLS,ImageUrlMLS)
            print("************************")
            i=i+1
            items['id'] = IdMLS_query_answer
            items["PropIdMLS"] = PropIdMLS
            items["ImageNumberMLS"] = ImageNumberMLS
            items["ImageTypeMLS"] = ImageTypeMLS
            items["ImageUrlMLS"]  = ImageUrlMLS
            items["ImageAltMLS"]  = ImageAltMLS
            IdMLS_query_answer = IdMLS_query_answer +1

            yield items

        # image_block_top = response.css("#carouselSection .aspectRatioImage")
        #
        # for images_single in image_block_top:
        #     ImageNumberMLS=images_single.css("div::attr(data-attachmentid)").get()
        #     ImageTypeMLS= images_single.css("div::attr(data-attachmenttypeid)").get()
        #     ImageUrlMLS = images_single.css("img::attr(src)").get()
        #     ImageAltMLS = images_single.css("img::attr(alt)").get()
        #     print("************************")
        #     print(i,ImageNumberMLS,ImageTypeMLS,ImageUrlMLS)
        #     print("************************")
        #     i=i+1
        #     items['id'] = IdMLS_query_answer
        #
        #     items['task_uid'] = my_task_id_from_database
        #     items["PropIdMLS"] = PropIdMLS
        #     items["ImageNumberMLS"] = ImageNumberMLS
        #     items["ImageTypeMLS"] = ImageTypeMLS
        #     items["ImageUrlMLS"]  = ImageUrlMLS
        #     items["ImageAltMLS"]  = ImageAltMLS
        #     IdMLS_query_answer = IdMLS_query_answer+ 1
        #
        #     yield items


