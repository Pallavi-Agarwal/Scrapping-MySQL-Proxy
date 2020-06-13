import scrapy
from ..items import FreelancerItem
import mysql.connector


class ScrapeHotel(scrapy.Spider):
    name = 'tables'
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


        PropIdMLS_query = 'SELECT PropIdMLS FROM zrdhrzmy_MLSData.property_mls_data where task_uid = "' + str(my_task_id_from_database[0][0]) + '"'
        cursor.execute(PropIdMLS_query)
        PropIdMLS_query_answer = cursor.fetchall()




        IdMLS_query = 'select * from zrdhrzmy_MLSData.rooms_mls_data order by id DESC LIMIT 1;'
        cursor.execute(IdMLS_query)
        IdMLS_query_answer = cursor.fetchall()

        if len(IdMLS_query_answer) != 0:
            IdMLS_query_answer = IdMLS_query_answer[0][0] + 1
        else:
            IdMLS_query_answer = 1

        print("*************************")
        print("THe Sequential Property id  is :",IdMLS_query_answer)
        print("****************************")




        cursor.close()
        mydb.close()

        PropIdMLS = PropIdMLS_query_answer[0][0]

        my_task_id_from_database = my_task_id_from_database[0][0]




        image_block = response.css("table.availabilityTable")
        imageCode = image_block.css("tr.rentalGridRow")
        i=1
        for images_single in imageCode:
            UniqueRoomKeyMLS = object()
            UniqueRoomKeyMLS =id(UniqueRoomKeyMLS)

            RoomTypeMLS=images_single.css("td.beds span.longText::text").get()
            RoomTypeMLS = ' '.join(RoomTypeMLS.split())

            BathroomTypeMLS= images_single.css("td.baths span.longText::text").get()
            BathroomTypeMLS = ' '.join(BathroomTypeMLS.split())

            RentRateMLS = images_single.css("td.rent::text").get()
            RentRateMLS = ' '.join(RentRateMLS.split())

            DepositMLS = images_single.css("td.deposit::text").get()
            DepositMLS = ' '.join(DepositMLS.split())

            AreaMLS = images_single.css("td.sqft::text").get()
            AreaMLS = ' '.join(AreaMLS.split())

            LeaseMLS = images_single.css("td.leaseLength::text").get()
            try:
                LeaseMLS = ' '.join(LeaseMLS.split())
            except:
                pass

            RoomNameMLS = images_single.css("td.name::text").get()
            RoomNameMLS = ' '.join(RoomNameMLS.split())

            StartMLS = images_single.css("td.available::text").get()
            StartMLS = ' '.join(StartMLS.split())


            i=i+1
            items['id'] = IdMLS_query_answer
            items['task_uid'] = my_task_id_from_database
            items["PropIdMLS"] = PropIdMLS
            items["UniqueRoomKeyMLS"] =UniqueRoomKeyMLS
            items["RoomTypeMLS"] = RoomTypeMLS
            items["BathroomTypeMLS"] = BathroomTypeMLS
            items["RentRateMLS"]  = RentRateMLS
            items["DepositMLS"]  = DepositMLS
            items["AreaMLS"] = AreaMLS
            items['LeaseMLS']= LeaseMLS
            items["RoomNameMLS"] = RoomNameMLS
            items["StartMLS"]=StartMLS

            IdMLS_query_answer = IdMLS_query_answer+1


            yield items


