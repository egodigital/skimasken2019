from server.models.achievement import AchievementModel, achievement_schema,achievements_schema, achievement_parser
from server.models.achievement_assignment import AchievementAssignmentModel, achievements_assignment_schema, \
    achievement_assignment_schema,achievement_assignment_parser
from server.models.experience_assignment import ExperienceModel,experience_schema,experience_assignment_parser,experiences_schema
from server.extensions.database import db

exp_gain=25
exp_loss=10

class ExperieceChecker:
    def __init__(self,session):
        self.session=session

    def update_experience(self,email,charging, car_sharer, reliability, eco_driver):
        #achievements_schema.dump(AchievementModel.query.all())

        experience_results=ExperienceModel.query.filter_by(email=email).first()
        #increase or decrease exp
        if charging:
            experience_results.charger_exp = experience_results.charger_exp + exp_gain
        else:
            experience_results.charger_exp = experience_results.charger_exp-exp_loss
        if car_sharer:
            experience_results.car_sharer_exp = experience_results.car_sharer_exp + exp_gain
        else:
            experience_results.car_sharer_exp = experience_results.car_sharer_exp-exp_loss
        if reliability:
            experience_results.reliability_exp = experience_results.reliability_exp + exp_gain
        else:
            experience_results.reliability_exp = experience_results.reliability_exp - exp_loss
        if eco_driver:
            experience_results.eco_driver_exp = experience_results.eco_driver_exp + exp_gain
        else:
            experience_results.eco_driver_exp = experience_results.eco_driver_exp - exp_loss


        #level checking
        if experience_results.eco_driver_exp< experience_results.eco_driver_level*experience_results.eco_driver_level*10:
            experience_results.eco_driver_level= experience_results.eco_driver_level-1
        elif experience_results.eco_driver_exp > (experience_results.eco_driver_level+1) * (experience_results.eco_driver_level+1)\
                    * 10:
                experience_results.eco_driver_level = experience_results.eco_driver_level + 1
        if experience_results.charger_exp< experience_results.charger_level*experience_results.charger_level*10:
            experience_results.charger_level= experience_results.charger_level-1
        elif experience_results.charger_exp > (experience_results.charger+1) * (experience_results.charger+1)\
                    * 10:
                experience_results.charger_level = experience_results.charger_level + 1
        if experience_results.car_sharer_exp< experience_results.car_sharer_level*experience_results.car_sharer_level*10:
            experience_results.car_sharer_level= experience_results.car_sharer_level-1
        elif experience_results.car_sharer_exp > (experience_results.car_sharer_level+1) * (experience_results.car_sharer_level+1)\
                    * 10:
                experience_results.car_sharer_level = experience_results.car_sharer_level + 1
        if experience_results.reliability_exp< experience_results.reliability_level*experience_results.reliability_level*10:
            experience_results.reliability_level= experience_results.reliability_level-1
        elif experience_results.reliability_exp > (experience_results.reliability_level+1) * (experience_results.reliability_level+1)\
                    * 10:
                experience_results.reliability_level = experience_results.reliability_level + 1
        self.session.commit()