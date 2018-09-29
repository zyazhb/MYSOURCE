<html>
<body>
<?php 
	stream_context_set_default( [
    	'ssl' => [
        	'verify_peer' => false,
       		'verify_peer_name' => false,
    	],
	]);
	
	$urllist=array("https://www.nefu.edu.cn","https://cas.nefu.edu.cn","https://nic.nefu.edu.cn","http://xxgk.nefu.edu.cn/","http://lib.nefu.edu.cn/");
	$temp=count($urllist);
	echo '<table width="900" border="1" height="20"><tr><td>服务器列表</td><td>当前状态</td></tr>';
	for($i=0;$i<$temp;$i++){ 
		$url=$urllist[$i];		
		$header_info=get_headers($url);
		echo '<tr><td>'.$url.'</td><td>'.$header_info[0].'</td></tr>';
		$maillist[$i]=$url.' status:  '.$header_info[0];
	}
	//print_r($maillist);
	$myresult=implode('<br>',$maillist);
?>
	<form ENCTYPE="multipart/form-data" ACTION="urltest.php" METHOD="POST">
	<input type='text' name='mailto' value='请输入您的邮箱'>
	<input type='checkbox' name='sendornot' value='发送邮件'>
	<input type='submit' value='提交'>
<?php
	if(isset($_POST['sendornot'])&&isset($_POST['mailto']))
	{
	echo "sent content:<br>".$myresult;
	mailtest($myresult,$_POST['mailto']);
	}
function mailtest($content,$mailto)
{
	require_once "Smtp.class.php";
	//******************** 配置信息 ********************************
	$smtpserver = "smtp.126.com";//SMTP服务器
	$smtpserverport =25;//SMTP服务器端口
	$smtpusermail = "zyazhbtest@126.com";//SMTP服务器的用户邮箱
	$smtpemailto = $mailto;//发送给谁
	$smtpuser = "zyazhbtest@126.com";//SMTP服务器的用户帐号，注：部分邮箱只需@前面的用户名
	$smtppass = "nefu1234";//SMTP服务器的用户密码
	$mailtitle = "NEFU主站状态报告";//邮件主题
	$mailcontent = "<h1>".$content."</h1>";//邮件内容
	$mailtype = "HTML";//邮件格式（HTML/TXT）,TXT为文本邮件
	//************************ 配置信息 ****************************
	$smtp = new Smtp($smtpserver,$smtpserverport,true,$smtpuser,$smtppass);//这里面的一个true是表示使用身份验证,否则不使用身份验证.
	$smtp->debug = false;//是否显示发送的调试信息
	$state = $smtp->sendmail($smtpemailto, $smtpusermail, $mailtitle, $mailcontent, $mailtype);

	echo "<div style='width:300px; margin:36px auto;'>";
	if($state==""){
		echo "对不起，邮件发送失败！请检查邮箱填写是否有误。";
		exit(); 
	}
	echo "恭喜！邮件发送成功！！";
	echo "</div>";
}
?>
</body>
</html>