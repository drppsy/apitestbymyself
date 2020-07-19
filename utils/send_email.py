import smtplib
from email.mime.text import MIMEText

class SendEmail:
    global send_user
    global email_host
    global password
    send_user = 'feta6@qq.com'
    email_host = 'smtp.qq.com'
    password = 'atmokxcmxptifjad'

    def send_mail(self, user_List, sub,content):
        user = '飞塔' + '<' + send_user + '>'
        server = smtplib.SMTP_SSL(email_host)
        server.ehlo(email_host)
        server.login(send_user,password)
        message = MIMEText(content,_subtype='plain',_charset='utf-8')
        message['Subject'] = sub
        message['From'] = user
        message['To'] = ";".join(user_List)

        server.sendmail(user,user_List,message.as_string())

    def send_main(self, pass_list, fail_list):
        pass_count = float(len(pass_list))
        fail_count = float(len(fail_list))
        num_count = pass_count + fail_count

        pass_rate = '{:.2%}'.format(pass_count*100/num_count)
        fail_rate = '{:.2%}'.format(fail_count*100/num_count)

        user_list = ['feta6@qq.com','19930212@163.com']
        sub = '游犀社区BBS-Staging接口自动化测试报告'
        content = '此次一共运行%s个用例，其中通过%s个用例，失败%s个用例，成功率为%s，失败率为%s' %(num_count,pass_count,fail_count,pass_rate,fail_rate)
        self.send_mail(user_list,sub,content)

if __name__ == '__main__':
    sen = SendEmail()
    # pass_list = ['1','2','3','4','5']
    # fail_list = ['6']
    # sen.send_main(pass_list,fail_list)