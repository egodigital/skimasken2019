from server.models.achievement import AchievementModel, achievement_schema,achievements_schema, achievement_parser
from server.extensions.database import db


def check_achievements_for_user(email):
    #achievement = achievement_schema.load(achievement_parser.parse_args(), session=db.session)
    #db.session.add(achievement)
    #db.session.commit()
    achievements_schema.dump(AchievementModel.query.all())
    print("hi")
    #for row in achievements:
    #    print("Name: ", row.achievement_id, "Address:", row.name, "Email:", row.score)
    #alle achievments suchen die man noch nicht hat

    #durch den rest iterieren und gucken ob was erfüllt

    #update in achievment assgment

    #score updaten

