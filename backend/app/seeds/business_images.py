from app.models import db, environment, SCHEMA, Business_Image


def seed_business_images():
    papajohns_image1 = Business_Image(
        business_id = 1,
        url = 'https://s3-media0.fl.yelpcdn.com/bphoto/2HNmXmstiAnwUDhZlWj8jg/l.jpg'
    )
    papajohns_image2 = Business_Image(
        business_id = 1,
        url = 'https://s3-media0.fl.yelpcdn.com/bphoto/KIxNxR4V4UCl-aBMj67Oog/l.jpg'
    )
    papajohns_image3 = Business_Image(
        business_id = 1,
        url = 'https://s3-media0.fl.yelpcdn.com/bphoto/EdbZ_ov61vGXvtz9kHLJpA/l.jpg'
    )
    tatsu_image1 = Business_Image(
        business_id = 2,
        url = 'https://s3-media0.fl.yelpcdn.com/bphoto/tkCV3_o4-D2Yxajk9d4MHQ/l.jpg'
    )
    tatsu_image2 = Business_Image(
        business_id = 2,
        url = 'https://s3-media0.fl.yelpcdn.com/bphoto/CDXgoD8xiqxm4_crLQk7kw/l.jpg'
    )
    tatsu_image3 = Business_Image(
        business_id = 2,
        url = 'https://s3-media0.fl.yelpcdn.com/bphoto/Hy7c4pch5EZJFvewFimrnA/o.jpg'
    )
    etta_image1 = Business_Image(
        business_id = 3,
        url = 'https://s3-media0.fl.yelpcdn.com/bphoto/C0MbfZGgO_2VgL09LHrC_w/l.jpg'
    )
    etta_image2 = Business_Image(
        business_id = 3,
        url = 'https://s3-media0.fl.yelpcdn.com/bphoto/Qzv1zbcSZkDtrrnAaAzjEA/l.jpg'
    )
    etta_image3 = Business_Image(
        business_id = 3,
        url = 'https://s3-media0.fl.yelpcdn.com/bphoto/YpqPObIOWxCw91ne_8Owuw/l.jpg'
    )
    five_guys_image1 = Business_Image(
        business_id = 4,
        url = 'https://s3-media0.fl.yelpcdn.com/bphoto/IaTE03zUWTnF4WSSw59hMw/348s.jpg'
    )
    five_guys_image2 = Business_Image(
        business_id = 4,
        url = 'https://s3-media0.fl.yelpcdn.com/bphoto/88MMCFqtw3G3u062ikiW9A/l.jpg'
    )
    five_guys_image3 = Business_Image(
        business_id = 4,
        url = 'https://s3-media0.fl.yelpcdn.com/bphoto/7tOruVB_bm4mlY54LStoBQ/o.jpg'
    )
    ini_image1 = Business_Image(
        business_id = 5,
        url = 'https://s3-media0.fl.yelpcdn.com/bphoto/6My8d_qQ4hQ3klHKzkgFHQ/l.jpg'
    )
    ini_image2 = Business_Image(
        business_id = 5,
        url = 'https://s3-media0.fl.yelpcdn.com/bphoto/2nCd8aguKiDFvWX6adT6dQ/l.jpg'
    )
    ini_image3 = Business_Image(
        business_id = 5,
        url = 'https://s3-media0.fl.yelpcdn.com/bphoto/tNQmPajCq0KudFLUpmshoQ/l.jpg'
    )
    the_beast_and_company_image1 = Business_Image(
        business_id = 6,
        url = 'https://s3-media0.fl.yelpcdn.com/bphoto/Xr9EucTmLMFFpCqsPUDOXA/l.jpg'
    )
    the_beast_and_company_image2 = Business_Image(
        business_id = 6,
        url = 'https://s3-media0.fl.yelpcdn.com/bphoto/ZeugZ5JtH1v4fKtJ0WuysQ/l.jpg'
    )
    the_beast_and_company_image3 = Business_Image(
        business_id = 6,
        url = 'https://s3-media0.fl.yelpcdn.com/bphoto/mNNB5aUH6iBbs8EAqAT81A/o.jpg'
    )

    db.session.add(papajohns_image1)
    db.session.add(papajohns_image2)
    db.session.add(papajohns_image3)
    db.session.add(tatsu_image1)
    db.session.add(tatsu_image2)
    db.session.add(tatsu_image3)
    db.session.add(etta_image1)
    db.session.add(etta_image2)
    db.session.add(etta_image3)
    db.session.add(five_guys_image1)
    db.session.add(five_guys_image2)
    db.session.add(five_guys_image3)
    db.session.add(ini_image1)
    db.session.add(ini_image2)
    db.session.add(ini_image3)
    db.session.add(the_beast_and_company_image1)
    db.session.add(the_beast_and_company_image2)
    db.session.add(the_beast_and_company_image3)
    db.session.commit()

def undo_business_images():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.business_images RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM business_images")

    db.session.commit()