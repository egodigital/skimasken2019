from server.models.achievement import AchievementModel, achievement_schema,achievements_schema, achievement_parser
from server.models.achievement_assignment import AchievementAssignmentModel, achievements_assignment_schema, \
    achievement_assignment_schema,achievement_assignment_parser
from server.models.experience_assignment import ExperienceModel,experience_schema,experience_assignment_parser,experiences_schema
from server.extensions.database import db

class ArchievementChecker:
    def __init__(self,session):
        self.session=session

    def check_achievements_for_user(self,email):
        achievements_assignments=[a.achievement_id for a in AchievementAssignmentModel.query.filter_by(user_email=email).all()]
        achievements = AchievementModel.query.filter(AchievementModel.achievement_id.notin_(achievements_assignments)).all()
        self.check_if_archieved(email, achievements)

        #TODO score updaten
    def check_if_archieved(self, email, achievement_query_result):
        experience_results=ExperienceModel.query.filter_by(email=email).first()
        for achievement in achievement_query_result:
            new_achievement_flag=False
            if achievement.type == "level":
                if achievement_query_result.level_type=="CHARGER":
                    if achievement_query_result.level_req==experience_results.charger_level:
                        achievement = achievement_assignment_schema.load({"email":email,"achievement_id":achievement.achievement_id}, session=self.session)
                        db.session.add(achievement)
                        new_achievement_flag=True
                if achievement_query_result.level_type=="CAR_SHARER":
                    if achievement_query_result.level_req==experience_results.car_sharer_level:
                        achievement = achievement_assignment_schema.load({"email":email,"achievement_id":achievement.achievement_id}, session=self.session)
                        db.session.add(achievement)
                        new_achievement_flag=True
                if achievement_query_result.level_type=="ECO_DRIVER":
                    if achievement_query_result.level_req==experience_results.eco_driver_level:
                        achievement = achievement_assignment_schema.load({"email":email,"achievement_id":achievement.achievement_id}, session=self.session)
                        db.session.add(achievement)
                        new_achievement_flag=True
                if achievement_query_result.level_type=="RELIABILITY":
                    if achievement_query_result.level_req==experience_results.reliability_level:
                        achievement = achievement_assignment_schema.load({"email":email,"achievement_id":achievement.achievement_id}, session=self.session)
                        db.session.add(achievement)
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

