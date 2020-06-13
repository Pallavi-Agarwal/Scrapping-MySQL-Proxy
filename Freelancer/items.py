# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FreelancerItem(scrapy.Item):
    # define the fields for your item here like:
    task_uid = scrapy.Field()
    PropIdMLS = scrapy.Field()
    PropertyNameMLS = scrapy.Field()
    PropertyAddressMLS = scrapy.Field()
    NeighborhoodMLS =scrapy.Field()
    PhoneNumberMLS =scrapy.Field()

    StudioSumPriceMLS =scrapy.Field()
    StudioSumPerMLS=scrapy.Field()

    Apt2SumPriceMLS=scrapy.Field()
    Apt2SumPerMLS=scrapy.Field()

    Apt3SumPriceMLS=scrapy.Field()
    Apt3SumPerMLS=scrapy.Field()

    Apt4SumPriceMLS=scrapy.Field()
    Apt4SumPerMLS=scrapy.Field()



    MonthlyFeeMLS=scrapy.Field()

    OneTimeFeeMLS=scrapy.Field()
    FreeUtilityMLS=scrapy.Field()
    DescriptionMLS = scrapy.Field()
    LeaseMLS = scrapy.Field()

    ParkingMLS = scrapy.Field()

    Day1MLS = scrapy.Field()
    #
    Day1HoursMLS = scrapy.Field()
    Day2MLS = scrapy.Field()
    Day2HoursMLS = scrapy.Field()
    Day3MLS = scrapy.Field()
    Day3HoursMLS = scrapy.Field()

    PropLogoMLS=scrapy.Field()

    UniqueMLS=scrapy.Field()

    FeaturesMLS =scrapy.Field()
    FitnessMLS =scrapy.Field()
    InteriorMLS =scrapy.Field()
    KitchenMLS =scrapy.Field()
    LivingMLS =scrapy.Field()
    OutdoorMLS =scrapy.Field()
    PetMLS =scrapy.Field()
    Pet2MLS =scrapy.Field()
    PropInfoMLS =scrapy.Field()
    SecurityMLS =scrapy.Field()
    ServiceMLS =scrapy.Field()
    StudentMLS =scrapy.Field()
    PropertyNameMLS1=scrapy.Field()
    ImageNumberMLS=scrapy.Field()
    ImageTypeMLS=scrapy.Field()
    ImageUrlMLS = scrapy.Field()
    ImageAltMLS = scrapy.Field()
    RoomTypeMLS = scrapy.Field()
    BathroomTypeMLS = scrapy.Field()
    RentRateMLS= scrapy.Field()
    DepositMLS = scrapy.Field()
    AreaMLS = scrapy.Field()
    RoomNameMLS = scrapy.Field()
    UniqueRoomKeyMLS = scrapy.Field()
    id = scrapy.Field()

    StartMLS = scrapy.Field()


