@echo off
echo ����-����ϵͳ�ӿ��Զ�������׼����ʼ......
@echo on



del /f /s /q  ./report/tmp/*.json
del /f /s /q  ./report/tmp/*.jpg


@echo off
echo �����ļ�ɾ��������ɣ���ʼ���нű�......
@echo on

G:
cd  ./test_case
pytest  -sq --alluredir=../report/tmp

allure serve ../report/tmp


@echo off
echo �ӿ��Զ������гɹ�
pause
 
