import mysql.connector


class FreelancerPipeline(object):
    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.spider.name)

    def __init__(self, spider_name):
        print(spider_name)
        if spider_name == "images":
            self.create_connection_image()
            # self.create_table_image()

        elif spider_name == "tables":
            self.create_connection_table()
            # self.create_table_table()

        elif spider_name == "quotes":
            self.create_connection_discrip()
            # self.create_table_discrip()

    def create_connection_image(self):
        self.conn = mysql.connector.connect(
            host="zrd.hrz.mybluehost.me",
            user="zrdhrzmy_star",
            passwd="safd$#SDF43",
            database="zrdhrzmy_MLSData"
        )
        self.curr = self.conn.cursor()

    def create_connection_table(self):
        self.conn = mysql.connector.connect(
            host="zrd.hrz.mybluehost.me",
            user="zrdhrzmy_star",
            passwd="safd$#SDF43",
            database="zrdhrzmy_MLSData"
        )
        self.curr = self.conn.cursor()

    def create_connection_discrip(self):
        self.conn = mysql.connector.connect(
            host="13.209.76.204",
            user="star",
            passwd="starstars",
            database="mlsdatabase"
        )
        self.curr = self.conn.cursor()

    def create_table_image(self):
        self.curr.execute("""DROP TABLE IF EXISTS image_mls_data""")
        self.curr.execute("""create table image_mls_data(
        id text,
        task_uid text,
        PropIdMLS text,
        ImageNumberMLS text,
        ImageTypeMLS text,
        ImageUrlMLS text,
        ImageAltMLS text        
        )
        """)

    def create_table_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS rooms_mls_data""")
        self.curr.execute("""create table rooms_mls_data(
                id text,
                task_uid text,
                PropIdMLS text,
                UniqueRoomKeyMLS text,
                RoomTypeMLS text,
                BathroomTypeMLS text,
                RentRateMLS text,
                DepositMLS text,
                AreaMLS text,
                LeaseMLS text,
                RoomNameMLS text,
                StartMLS text
        )
        """)

    def create_table_discrip(self):
        self.curr.execute("""DROP TABLE IF EXISTS property_mls_data""")
        self.curr.execute("""create table property_mls_data(
        id text,
        task_uid text,
        PropIdMLS text,
        PropertyNameMLS text,
        PropertyAddressMLS text,
        NeighborhoodMLS text,
        PhoneNumberMLS text,
        StudioSumPriceMLS text,
        StudioSumPerMLS text,
        Apt2SumPriceMLS text,
        Apt2SumPerMLS text,
        Apt3SumPriceMLS text,
        Apt3SumPerMLS text,
        Apt4SumPriceMLS text,
        Apt4SumPerMLS text,
        MonthlyFeeMLS text,
        OneTimeFeeMLS text,
        FreeUtilityMLS text,
        DescriptionMLS text,
        LeaseMLS text,
        ParkingMLS text,
        Day1MLS text,
        Day1HoursMLS text,
        Day2MLS text,
        Day2HoursMLS text,
        Day3MLS text,
        Day3HoursMLS text,
        PropLogoMLS text,
        UniqueMLS text,
        FeaturesMLS text,
        FitnessMLS text,
        InteriorMLS text,
        KitchenMLS text,
        LivingMLS text,
        OutdoorMLS text,
        PetMLS text,
        Pet2MLS text,
        PropInfoMLS text,
        SecurityMLS text,
        ServiceMLS text
          )
          """)

    def process_item(self, item, spider):
        print(spider.name)
        if spider.name == "images":

            self.store_db_image(item)
            return item
        elif spider.name == "tables":

            self.store_db_table(item)
            return item
        elif spider.name == "quotes":

            self.store_db_discrip(item)
            return item

    def store_db_image(self, item):
        self.curr.execute("""insert into image_mls_data values (%s,%s,%s,%s,%s,%s,%s)""", (
            item['id'],
            item["task_uid"],
            item["PropIdMLS"],
            item["ImageNumberMLS"],
            item["ImageTypeMLS"],
            item["ImageUrlMLS"],
            item["ImageAltMLS"]
        ))
        self.conn.commit()

    def store_db_table(self, items):
        self.curr.execute("""insert into rooms_mls_data values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (
            items["id"],
            items["task_uid"],
            items["PropIdMLS"],
            items["UniqueRoomKeyMLS"],
            items["RoomTypeMLS"],
            items["BathroomTypeMLS"],
            items["RentRateMLS"],
            items["DepositMLS"],
            items["AreaMLS"],
            items['LeaseMLS'],
            items["RoomNameMLS"],
            items["StartMLS"],
        ))
        self.conn.commit()

    def store_db_discrip(self, items):

        self.curr.execute(
            """insert into property_mls_data values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
            (   items["id"],
                items["task_uid"],
                items["PropIdMLS"],
                items["PropertyNameMLS"],
                items["PropertyAddressMLS"],
                items["NeighborhoodMLS"],
                items["PhoneNumberMLS"],
                items["StudioSumPriceMLS"],
                items["StudioSumPerMLS"],
                items["Apt2SumPriceMLS"],
                items["Apt2SumPerMLS"],
                items["Apt3SumPriceMLS"],
                items["Apt3SumPerMLS"],
                items["Apt4SumPriceMLS"],
                items["Apt4SumPerMLS"],
                items["MonthlyFeeMLS"],
                items["OneTimeFeeMLS"],
                items["FreeUtilityMLS"],
                items["DescriptionMLS"],
                items["LeaseMLS"],
                items["ParkingMLS"],
                items["Day1MLS"],
                items["Day1HoursMLS"],
                items["Day2MLS"],
                items["Day2HoursMLS"],
                items["Day3MLS"],
                items["Day3HoursMLS"],
                items["PropLogoMLS"],
                items["UniqueMLS"],
                items["FeaturesMLS"],
                items["FitnessMLS"],
                items["InteriorMLS"],
                items["KitchenMLS"],
                items["LivingMLS"],
                items["OutdoorMLS"],
                items["PetMLS"],
                items["Pet2MLS"],
                items["PropInfoMLS"],
                items["SecurityMLS"],
                items["ServiceMLS"]

            ))

        self.conn.commit()
