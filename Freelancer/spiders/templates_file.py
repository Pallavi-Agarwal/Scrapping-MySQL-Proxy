import scrapy
from ..items import FreelancerItem
import re
class ScrapeHotel(scrapy.Spider):
    name = 'rough'
    start_urls = [
        'https://www.apartments.com/lenox-at-patterson-place-durham-nc/4s7tmgl/'
    ]

    def parse(self, response):
        items = FreelancerItem()
        StudioSumPriceMLS = response.css(".rentRollup:nth-child(1)::text").extract()
        StudioSumPriceMLS = [x.rstrip() for x in StudioSumPriceMLS]
        StudioSumPriceMLS = [x.replace("\r", "") for x in StudioSumPriceMLS]
        StudioSumPriceMLS = [x.replace("\n", "") for x in StudioSumPriceMLS]
        StudioSumPriceMLS = [x.replace("\t", "") for x in StudioSumPriceMLS]

        newList =[]
        for i in StudioSumPriceMLS:
            if len(i)!=0:
                newList.append(i)

        StudioSumPriceMLS = newList[0]


        print(StudioSumPriceMLS)


        # bullets = response.css("div.specList")
        # num=1
        # nameList = ["FeaturesMLS", "FitnessMLS", "InteriorMLS", "KitchenMLS", "LeaseMLS", "LivingMLS", "OutdoorMLS",
        #             "ParkingMLS", "PetMLS", "PropInfoMLS", "SecurityMLS", "ServiceMLS", "StudentMLS", "UniqueMLS"]
        #
        # for i in nameList:
        #     items[i]=''
        #
        # for i in bullets:
        #     print("************************************************************")
        #     # print(i.extract())
        #     for j in (i.css("h3::text")):
        #         if j.extract()==i.css("h3::text").extract()[0]:
        #             print("I got that ",j.extract(), num)
        #             key = j.extract()
        #             if key =="Unique Features":
        #                 name = "UniqueMLS"
        #                 var = name
        #
        #
        #             elif key == "Pet Policy":
        #                 name = "PetMLS"
        #                 var = name
        #
        #             elif key == "Parking" :
        #                 name = "ParkingMLS"
        #                 var = name
        #
        #             elif key == "Property Information":
        #                 name = "PropInfoMLS"
        #                 var = name
        #
        #
        #             elif key == "Lease Length" :
        #                 name  = "LeaseMLS"
        #                 var = name
        #
        #
        #
        #             elif key == "Services" :
        #                 name = "ServiceMLS"
        #
        #             elif key == "Interior" :
        #                 name = "InteriorMLS"
        #                 var = name
        #
        #
        #             elif key == "Outdoor Space" :
        #                 name = "OutdoorMLS"
        #                 var = name
        #
        #
        #             elif key == "Fitness & Recreation" :
        #                 name = "FitnessMLS"
        #                 var = name
        #
        #
        #             elif key == "Features":
        #                 name = "FeaturesMLS"
        #                 var = name
        #
        #
        #             elif key == "Kitchen":
        #                 name =  "KitchenMLS"
        #                 var = name
        #
        #
        #
        #             elif key == "Living Space":
        #                 name = "LivingMLS"
        #                 var = name
        #
        #
        #             elif key == "Security":
        #                 name =  "SecurityMLS"
        #                 var = name
        #
        #             if name != "ParkingMLS":
        #
        #                 items[name] = response.css("div.specList:nth-child(" + str(num) + ") ul li::text").extract()
        #                 items[name] = ', '.join(items[name])
        #             else:
        #                 print(name)
        #                 prop1 = response.css("div.specList:nth-child(" + str(num) + ") h4::text").extract()
        #                 prop2 = response.css(
        #                     "div.specList:nth-child(" + str(num) + ") p::text").extract()
        #
        #
        #
        #
        #                 for i in prop2:
        #
        #                     prop2 = i.replace("[", "")
        #                     prop2 = prop2.replace("]", "")
        #                     import re
        #
        #                     prop2 = re.sub('\s+', ' ', prop2)
        #                     prop2 = ' '.join(prop2.split())
        #                     prop2 = re.sub('\s+', ' ', prop2)
        #
        #                     prop2 = re.sub('\s+', ' ', prop2)
        #
        #                 for i in prop1:
        #
        #                     prop1 = i.replace("[", "")
        #                     prop1 = prop1.replace("]", "")
        #                     import re
        #
        #                     prop1 = re.sub('\s+', ' ', prop1)
        #                     prop1 = ' '.join(prop1.split())
        #                     prop1 = re.sub('\s+', ' ', prop1)
        #
        #                     prop1 = re.sub('\s+', ' ', prop1)
        #
        #                 print(prop1)
        #                 print(prop2)
        #
        #
        #                 prop3 = prop1+","+prop2
        #                 items[name] = prop3
        #
        #             num = num +1
        #         else:
        #             pass
        #             # print(i.css("h3::text").extract())
        #     print("************************************************************")
        #
        #
        # print(items['UniqueMLS'])










