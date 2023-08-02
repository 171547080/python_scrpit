import sys 
sys.path.append("..")  
import ai_predict_test as AI_API 

#img_dir=r"D:\工作交接\智慧工地\训练集\反光衣\SafetyVest\0727\GD_vest_train_20230728113945\opt\gongdi\biaozhu\image\val"
img_dir=r"D:\工作交接\智慧工地\误报数据\中医医院\TD_blue_helmet_train_20230726163353\opt\gongdi\biaozhu\image\val"
TARGET_AI_TASK_ID="8f97a571-22e5-41e3-afed-8f525d8338af"
COMPARE_AI_TASK_ID="e9e35528-71c7-4b62-9b88-8970bee55ab6"
# 主函数
if __name__ == "__main__":
    AI_API.setSkipPredict(False)
    AI_API.check_ai_models(img_dir,TARGET_AI_TASK_ID,COMPARE_AI_TASK_ID)