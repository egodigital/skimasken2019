from server.models.achievement import AchievementModel, achievement_schema,achievements_schema, achievement_parser
from server.models.achievement_assignment import AchievementAssignmentModel, achievements_assignment_schema, \
    achievement_assignment_schema,achievement_assignment_parser
from server.models.experience_assignment import ExperienceModel,experience_schema,experience_assignment_parser,experiences_schema
from server.extensions.database import db

class ArchievementChecker:
    def __init__(self,session):
        self.session=session

    def check_achievements_for_user(self,email):
        #error when empty
        #TODO hardcode
        #achievement=AchievementModel.query.filter_by(achievement_id=5).first()
        #db.session.add(achievement)
        #db.session.commit()
        #achievements_schema.dump(AchievementModel.query.all())
        achievements_assignments=[a.achievement_id for a in AchievementAssignmentModel.query.filter_by(user_email=email).all()]

        achievements = AchievementModel.query.filter(AchievementModel.achievement_id.notin_(achievements_assignments)).all()

        self.check_if_archieved(email, achievements)
        for row in achievements:
            print("ID: ", row.achievement_id, "Email: ", row.name)
        #score updaten
    def check_if_archieved(self, email, achievement_query_result):
        for achievement in achievement_query_result:
            new_achievement_flag=False
            if achievement.type == "level":
                if True:   #leveltype req
                    new_achievement_flag=True
            if achievement.type == "simple":
                #switch case mit jederm achievement
                if False:
                    new_achievement_flag=True
            if new_achievement_flag:
                #add in achievement_assigment

                achievement_assignment_new_achievement = achievement_assignment_schema.load({"user_email":email,"achievement_id":achievement.achievement_id}, session=self.session)
                self.session.add(achievement_assignment_new_achievement)
                self.session.commit()

