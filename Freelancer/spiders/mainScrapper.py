import scrapy
import mysql.connector

import re
from ..items import FreelancerItem

class ScrapeHotel(scrapy.Spider):
    name = 'quotes'
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

    def remove(self,string):
        return string.replace(" ", "")

        # Driver Program


    def parse(self, response):
        items = FreelancerItem()

        my_url_starting = response.request.url
        host = "13.209.76.204",
        user = "star",
        passwd = "starstars",
        database = "mlsdatabase"

        mydb = mysql.connector.connect(host="13.209.76.204", user="star", passwd="starstars",
                                       database="mlsdatabase")
        cursor = mydb.cursor()
        sql_select_Query = 'SELECT task_uid FROM mlsdatabase.task_queue where url = "' + str(my_url_starting) + '"'
        cursor.execute(sql_select_Query)
        my_task_id_from_database = cursor.fetchall()

        IdMLS_query = 'select * from mlsdatabase.property_mls_data order by id DESC LIMIT 1;'
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
        print("*****************")
        print(my_task_id_from_database)
        print("*****************")

        PropIdMLS = my_url_starting
        PropIdMLS = id(PropIdMLS)
        PropertyNameMLS  = response.css("h1.propertyName::text").extract()
        PropertyNameMLS=PropertyNameMLS[0]
        PropertyNameMLS = ' '.join(PropertyNameMLS.split())
        print("*****************")
        print(PropertyNameMLS)
        print("*****************")



        PropertyAddressMLS = response.css("div.propertyAddress span::text").extract()
        PropertyAddressMLS = PropertyAddressMLS[0]+","+PropertyAddressMLS[1]+","+PropertyAddressMLS[2]+"," + PropertyAddressMLS[3]
        print("*****************")
        print(PropertyAddressMLS)
        print("*****************")

        NeighborhoodMLS  = response.css("a.neighborhood::text").extract()

        print("*****************")
        print(NeighborhoodMLS)
        print("*****************")
        import re
        PhoneNumberMLS  = response.css("#ctn::text").extract()
        PhoneNumberMLS = PhoneNumberMLS[0]
        print(PhoneNumberMLS)
        try:
            StudioSumPriceMLS = response.css(".rentRollup:nth-child(1)::text").extract()
            StudioSumPriceMLS = [x.rstrip() for x in StudioSumPriceMLS]
            StudioSumPriceMLS = [x.replace("\r", "") for x in StudioSumPriceMLS]
            StudioSumPriceMLS = [x.replace("\n", "") for x in StudioSumPriceMLS]
            StudioSumPriceMLS = [x.replace("\t", "") for x in StudioSumPriceMLS]

            newList = []
            for i in StudioSumPriceMLS:
                if len(i) != 0:
                    newList.append(i)

            StudioSumPriceMLS = newList[0]

            print(StudioSumPriceMLS)


            print("*****************")
            print("StudioSumPriceMLS",StudioSumPriceMLS)
            print("*****************")
        except:
            pass
        print(StudioSumPriceMLS,type(StudioSumPriceMLS))
        StudioSumPerMLS  = response.css(".rentRollup:nth-child(1) span:nth-child(2)::text").extract()

        try:
            StudioSumPerMLS=StudioSumPerMLS[0]
            StudioSumPerMLS=StudioSumPerMLS.replace("/","")
            if len(StudioSumPerMLS)==0:
                StudioSumPerMLS=''

            print(StudioSumPerMLS,type(StudioSumPerMLS))
            print("**********************************")
        except:
            pass


        try:
            Apt2SumPriceMLS = response.css(".rentRollup:nth-child(2)::text").extract()
            print(Apt2SumPriceMLS)
            Apt2SumPriceMLS = [x.rstrip() for x in Apt2SumPriceMLS]
            Apt2SumPriceMLS = [x.replace("\r", "") for x in Apt2SumPriceMLS]
            Apt2SumPriceMLS = [x.replace("\n", "") for x in Apt2SumPriceMLS]
            Apt2SumPriceMLS = [x.replace("\t", "") for x in Apt2SumPriceMLS]

            newList = []
            for i in Apt2SumPriceMLS:
                if len(i) != 0:
                    newList.append(i)

            Apt2SumPriceMLS = newList[0]

            print(Apt2SumPriceMLS)
        except:
            pass

        print(Apt2SumPriceMLS,type(Apt2SumPriceMLS))
        try:
            Apt2SumPerMLS  = response.css(".rentRollup:nth-child(2) span:nth-child(2)::text").extract()
            Apt2SumPerMLS = [x.rstrip() for x in Apt2SumPerMLS]
            Apt2SumPerMLS = [x.replace("\r", "") for x in Apt2SumPerMLS]
            Apt2SumPerMLS = [x.replace("\n", "") for x in Apt2SumPerMLS]
            Apt2SumPerMLS = [x.replace("\t", "") for x in Apt2SumPerMLS]

            newList = []
            for i in Apt2SumPerMLS:
                if len(i) != 0:
                    newList.append(i)

            Apt2SumPerMLS = newList[0]

            print(Apt2SumPerMLS)
        except:
            pass

        try:

            Apt3SumPriceMLS  = response.css(".rentRollup:nth-child(3)::text").extract()
            Apt3SumPriceMLS = [x.rstrip() for x in Apt3SumPriceMLS]
            Apt3SumPriceMLS = [x.replace("\r", "") for x in Apt3SumPriceMLS]
            Apt3SumPriceMLS = [x.replace("\n", "") for x in Apt3SumPriceMLS]
            Apt3SumPriceMLS = [x.replace("\t", "") for x in Apt3SumPriceMLS]

            newList = []
            for i in Apt3SumPriceMLS:
                if len(i) != 0:
                    newList.append(i)

            Apt3SumPriceMLS = newList[0]

            print(Apt3SumPriceMLS)
        except:
            pass

        try:

            Apt3SumPerMLS  = response.css(".rentRollup:nth-child(3) span:nth-child(2)::text").extract()
            Apt3SumPerMLS=Apt3SumPerMLS[0]
            Apt3SumPerMLS=Apt3SumPerMLS.replace("/","")

            print("**********************************")
            if len(Apt3SumPerMLS)==0:
                Apt3SumPerMLS=''
            print(Apt3SumPerMLS,type(Apt3SumPerMLS))
            print("**********************************")
        except:
            pass



        try:
            Apt4SumPriceMLS  = response.css(".rentRollup:nth-child(4)::text").extract()
            Apt4SumPriceMLS = [x.rstrip() for x in Apt4SumPriceMLS]
            Apt4SumPriceMLS = [x.replace("\r", "") for x in Apt4SumPriceMLS]
            Apt4SumPriceMLS = [x.replace("\n", "") for x in Apt4SumPriceMLS]
            Apt4SumPriceMLS = [x.replace("\t", "") for x in Apt4SumPriceMLS]

            newList = []
            for i in Apt4SumPriceMLS:
                if len(i) != 0:
                    newList.append(i)

            Apt4SumPriceMLS = newList[0]

            print(Apt4SumPriceMLS)
        except:
            if len(Apt4SumPriceMLS)==0:
                Apt4SumPriceMLS=''


        try:
            Apt4SumPerMLS  = response.css(".rentRollup:nth-child(4) span:nth-child(2)::text").extract()
            Apt4SumPerMLS=Apt4SumPerMLS[0]
            Apt4SumPerMLS=Apt4SumPerMLS.replace("/","")

            print("**********************************")
            if len(Apt4SumPerMLS)==0:

                Apt4SumPerMLS=''
            print(Apt4SumPerMLS)
            print("**********************************")
        except:
            if len(Apt4SumPerMLS)==0:
                Apt4SumPerMLS=''
            pass

        try:

            MonthlyFeeMLS  = response.css(".monthlyFees span::text").extract()
            ans=""
            for i in MonthlyFeeMLS:
                ans=ans+i+" "
            MonthlyFeeMLS=ans
            MonthlyFeeMLS=(MonthlyFeeMLS[:int(len(MonthlyFeeMLS) / 2)])
            print("**********************************")
            print(MonthlyFeeMLS)
            print("**********************************")
        except:
            pass

        try:
            OneTimeFeeMLS  = response.css(".oneTimeFees span::text").extract()
            ans=""
            for i in OneTimeFeeMLS:
                ans=ans+i +" "
            OneTimeFeeMLS=ans
            OneTimeFeeMLS=(OneTimeFeeMLS[:int(len(OneTimeFeeMLS) / 2)])
            print("**********************************")
            print(OneTimeFeeMLS)
            print("**********************************")
        except:
            pass



        FreeUtilityMLS  = response.css(".freeUtilities span::text").extract()
        ans=""
        for i in FreeUtilityMLS:
            ans=ans+i +" "
        FreeUtilityMLS=ans
        FreeUtilityMLS=(FreeUtilityMLS[:int(len(FreeUtilityMLS) / 2)])


        print("**********************************")
        print(FreeUtilityMLS)
        print("**********************************")


        DescriptionMLS  = response.css("#descriptionSection p::text").extract()
        DescriptionMLS=str(DescriptionMLS[0])
        print("**********************************")
        print(DescriptionMLS,type(DescriptionMLS))
        print(type(DescriptionMLS))
        print("**********************************")




        # FeaturesMLS = response.css("div.specList:nth-child(10) ul li::text").extract()
        # FeaturesMLS = ', '.join(FeaturesMLS)
        # FeaturesMLS=str(FeaturesMLS)
        #
        # FitnessMLS = response.css("div.specList:nth-child(8) ul li::text").extract()
        # FitnessMLS = ', '.join(FitnessMLS)
        #
        #
        # InteriorMLS = response.css("div.specList:nth-child(6) ul li::text").extract()
        # InteriorMLS = ', '.join(InteriorMLS)
        #
        # KitchenMLS = response.css("div.specList:nth-child(11) ul li::text").extract()
        # KitchenMLS = ', '.join(KitchenMLS)
        #
        # LeaseMLS  = response.css(".leaseLength::text").extract()
        # lease=""
        # for i in LeaseMLS:
        #     lease= i + ","+lease
        #
        # LeaseMLS=lease
        # LeaseMLS=(LeaseMLS[:int(len(LeaseMLS) / 2)])
        #
        #
        #
        # LivingMLS = response.css("div.specList:nth-child(12) ul li::text").extract()
        # LivingMLS = ', '.join(LivingMLS)
        #
        #
        #
        # OutdoorMLS = response.css("div.specList:nth-child(7) ul li::text").extract()
        # OutdoorMLS = ', '.join(OutdoorMLS)
        #
        #
        # ParkingMLS = response.css(".parkingTypeFeeContainer h4::text").extract()
        # ParkingMLS=ParkingMLS[0].replace("  ","")
        # ParkingMLS=' '.join(ParkingMLS.split())
        #
        #
        # print("**********************************")
        # print(ParkingMLS)
        # print("**********************************")
        #
        #
        # PetMLS = response.css("div.specList:nth-child(2) h3+ .petPolicyDetails ul li::text").extract()
        #
        # PetMLS = ', '.join(PetMLS)
        #
        #
        # Pet2MLS = response.css("div.petPolicyDetails ul li::text").extract()
        # Pet2MLS = ', '.join(Pet2MLS)
        #
        #
        # PropInfoMLS = response.css("div.specList:nth-child(4) ul li::text").extract()
        # PropInfoMLS = ', '.join(PropInfoMLS)
        #
        #
        # SecurityMLS = response.css("div.specList:nth-child(13) ul li::text").extract()
        # SecurityMLS = ', '.join(SecurityMLS)
        #
        # ServiceMLS = response.css("div.specList:nth-child(5) ul li::text").extract()
        # ServiceMLS = ', '.join(ServiceMLS)
        #
        #
        # StudentMLS = response.css("div.specList:nth-child(9) ul li::text").extract()
        # StudentMLS = ', '.join(StudentMLS)
        # print(StudentMLS,type(Apt3SumPerMLS))
        #
        #
        # UniqueMLS = response.css("div.specList:nth-child(1) ul li::text ").extract()
        # UniqueMLS = ', '.join(UniqueMLS)
        bullets = response.css("div.specList")
        num=1
        nameList = ["FeaturesMLS", "FitnessMLS", "InteriorMLS", "KitchenMLS", "LeaseMLS", "LivingMLS", "OutdoorMLS",
                    "ParkingMLS", "PetMLS","Pet2MLS", "PropInfoMLS", "SecurityMLS", "ServiceMLS", "StudentMLS", "UniqueMLS"]

        for i in nameList:
            items[i]=""

        for i in bullets:
            print("************************************************************")
            # print(i.extract())
            for j in (i.css("h3::text")):
                if j.extract()==i.css("h3::text").extract()[0]:
                    print("I got that ",j.extract(), num)
                    key = j.extract()
                    if key =="Unique Features":
                        name = "UniqueMLS"
                        var = name


                    elif key == "Pet Policy":
                        name = "PetMLS"
                        name2 = "Pet2MLS"
                        var = name

                    elif key == "Parking" :
                        name = "ParkingMLS"
                        var = name

                    elif key == "Property Information":
                        name = "PropInfoMLS"
                        var = name


                    elif key == "Lease Length" :
                        name  = "LeaseMLS"
                        var = name



                    elif key == "Services" :
                        name = "ServiceMLS"

                    elif key == "Interior" :
                        name = "InteriorMLS"
                        var = name


                    elif key == "Outdoor Space" :
                        name = "OutdoorMLS"
                        var = name


                    elif key == "Fitness & Recreation" :
                        name = "FitnessMLS"
                        var = name


                    elif key == "Features":
                        name = "FeaturesMLS"
                        var = name


                    elif key == "Kitchen":
                        name =  "KitchenMLS"
                        var = name



                    elif key == "Living Space":
                        name = "LivingMLS"
                        var = name


                    elif key == "Security":
                        name =  "SecurityMLS"
                        var = name

                    print("&&&&&&&&&&&&&&&&&&&&&&&")
                    print("Finally I got ",key)
                    print("&&&&&&&&&&&&&&&&&&&&&&&")


                    if name=="ParkingMLS":
                        print(name)
                        prop1 = response.css("div.specList:nth-child(" + str(num) + ") h4::text").extract()
                        prop2 = response.css(
                            "div.specList:nth-child(" + str(num) + ") p::text").extract()
                        print(prop1)
                        print(prop2)



                        for i in prop2:

                            prop2 = i.replace("[", "")
                            prop2 = prop2.replace("]", "")
                            import re

                            prop2 = re.sub('\s+', ' ', prop2)
                            prop2 = ' '.join(prop2.split())
                            prop2 = re.sub('\s+', ' ', prop2)

                            prop2 = re.sub('\s+', ' ', prop2)

                        for i in prop1:

                            prop1 = i.replace("[", "")
                            prop1 = prop1.replace("]", "")
                            import re

                            prop1 = re.sub('\s+', ' ', prop1)
                            prop1 = ' '.join(prop1.split())
                            prop1 = re.sub('\s+', ' ', prop1)

                            prop1 = re.sub('\s+', ' ', prop1)

                        print(prop1)
                        print(prop2)
                        prop3 = prop1+","+prop2
                        items[name] = prop3






                        num = num +1
                    elif name == "PetMLS":

                        items[name] = response.css("div.specList:nth-child(" + str(num) + ") ul li::text").extract()
                        items[name] = ', '.join(items[name])
                        pet2 = response.css("div.specList:nth-child(" + str(num) + ") p::text").extract()

                        pet2 = [x.rstrip() for x in pet2]
                        pet2 = [x.replace("\r", "") for x in pet2]
                        pet2 = [x.replace("\n", "") for x in pet2]
                        pet2 = [x.replace("\t", "") for x in pet2]
                        import re

                        newList = []
                        for i in pet2:
                            if len(i) != 0:
                                newList.append(i)

                        pet2 = newList[0]



                        print(pet2)
                        items[name2] = pet2


                        num = num + 1

                    else:
                        items[name] = response.css("div.specList:nth-child(" + str(num) + ") ul li::text").extract()
                        items[name] = ', '.join(items[name])
                        num = num+1
                    # print(i.css("h3::text").extract())
            print("************************************************************")

        Day1MLS = response.css(".daysHoursContainer:nth-child(1) .days::text").extract()
        Day1MLS=Day1MLS[0].replace("  ","")

        Day1MLS=' '.join(Day1MLS.split())

        Day1HoursMLS = response.css(".daysHoursContainer:nth-child(1) .hours::text").extract()
        Day1HoursMLS=Day1HoursMLS[0].replace(" ","")
        Day1HoursMLS=' '.join(Day1HoursMLS.split())

        Day2MLS = response.css(".daysHoursContainer:nth-child(2) .days::text").extract()
        Day2MLS=Day2MLS[0].replace("  ","")
        Day2MLS=' '.join(Day2MLS.split())


        Day2HoursMLS = response.css(".daysHoursContainer:nth-child(2) .hours::text").extract()
        Day2HoursMLS=Day2HoursMLS[0].replace("  ","")
        Day2HoursMLS=' '.join(Day2HoursMLS.split())

        Day3MLS = response.css(".daysHoursContainer:nth-child(3) .days::text").extract()
        Day3MLS=Day3MLS[0].replace("  ","")
        Day3MLS=' '.join(Day3MLS.split())

        Day3HoursMLS = response.css(".daysHoursContainer:nth-child(3) .hours::text").extract()
        Day3HoursMLS=Day3HoursMLS[0].replace("  ","")
        Day3HoursMLS=' '.join(Day3HoursMLS.split())

        PropLogoMLS = response.css("div.officeHoursWrapper img::attr(src)").get()
        print("************************")
        print(PropLogoMLS)
        print("************************")

        # table_web =response.css("tr.rentalGridRow")
        #
        # for table_code in table_web:
        #     print("#####################")
        #     each_row=table_code.css(".beds longtext::text").extract()
        #     print(each_row)
        #     print("#####################")

        items["id"] = IdMLS_query_answer
        items['task_uid']=my_task_id_from_database
        items["PropIdMLS"] = PropIdMLS

        items["PropertyNameMLS"] = PropertyNameMLS
        items["PropertyAddressMLS"] = PropertyAddressMLS
        items["NeighborhoodMLS"] = NeighborhoodMLS[0]

        items["PhoneNumberMLS"] = PhoneNumberMLS

        items["StudioSumPriceMLS"] = StudioSumPriceMLS
        items["StudioSumPerMLS"] = StudioSumPerMLS

        items["Apt2SumPriceMLS"] = Apt2SumPriceMLS
        items["Apt2SumPerMLS"] = Apt2SumPerMLS

        items["Apt3SumPriceMLS"] = Apt3SumPriceMLS
        items["Apt3SumPerMLS"] = Apt3SumPerMLS

        items["Apt4SumPriceMLS"] = Apt4SumPriceMLS
        items["Apt4SumPerMLS"] = Apt4SumPerMLS


        items["MonthlyFeeMLS"] = MonthlyFeeMLS
        items["OneTimeFeeMLS"] = OneTimeFeeMLS

        items["FreeUtilityMLS"] = FreeUtilityMLS
        items["DescriptionMLS"] = DescriptionMLS


        items["Day1MLS"]=Day1MLS
        items["Day1HoursMLS"]=Day1HoursMLS

        items["Day2MLS"] = Day2MLS
        items["Day2HoursMLS"] = Day2HoursMLS

        items["Day3MLS"] = Day3MLS
        items["Day3HoursMLS"] = Day3HoursMLS

        items["PropLogoMLS"]=PropLogoMLS




        yield items


