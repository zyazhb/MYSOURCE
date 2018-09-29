<html>
<head>
<title>空课表生成器 BY-ZYA</title>
<head>
<body>
<?php
function isFree($thisweek,$thisxq,$thiskj)
		{
			if(isset($_POST['thisweek'])) $thisweek=$_POST['thisweek']; else $thisweek=1;
			$db=mysqli_connect('localhost','root','admin','zya') or die("cant connect".mysql_error($db));
			$sql = "SELECT * FROM kebiao";
			$result=mysqli_query($db,$sql);
			$all_tag=0;
			$all_tag1=0;
			$gathered=[];
			$kj=array(array("01","02"),array("03","04"),array("05","06"),array("07","08"),array("09","10"),array("11","12"));
			$transkj=$kj[$thiskj];
			while($row=mysqli_fetch_assoc($result))
			{ 
				$weektime=$row['SKZC'];							   //weektime[1-3,6-9,11,15]
				$result3=[];
			
				$wt_1=explode(',',$weektime);					   //wt1[[1-3],[6-9],[11],[15]]
				$ele_num=count($wt_1);
				for($i=0;$i<$ele_num;$i++)                         //外循环 ，分隔的数组
				{	
					if (!strstr($wt_1[$i],"-"))
						$result1[$i]=$wt_1[$i]; 				   //将不含-的数组保存到result1 [11][15]
					else{	
						$wt_2=explode('-',$wt_1[$i]);              //第二次处理 -分隔 [1][3]
				
						for($n=$wt_2[0],$tag=0;$n<=$wt_2[1];$n++,$tag++)
						$result2[$tag]=$n;						   //将周数补全
						}
						$result3=array_merge($result2,$result3);   //合并补全后的周数
						$result3=array_unique($result3);		   //去重
						$result2=[];							   //清空临时数组
					
				}
				if(isset($result1))							       //如果存在result1 再合并一次数据
					$result3=array_merge($result3,$result1);
			
				$classtime=$row['SKSJ'];
				$splited_xq=$classtime[0];						   //星期数
				$splited_row=str_split(substr($classtime,1,10),2); //分离节数
			
			//print_r ($splited_row);
			
				$all_gathered[$all_tag1]=$row["XSXM"];			   //汇总全部学生姓名
				$all_tag1++;
				
				$transkj1=in_array($transkj[0],$splited_row);
				$transkj2=in_array($transkj[1],$splited_row);
				if(in_array($thisweek, $result3) and ($classtime!=0) and  ($splited_xq[0]==$thisxq) and $transkj1 and $transkj2){//result3是该学生此课程的全部上课周数 如果该学生这周无课
					
					$gathered[$all_tag]=$row["XSXM"];			   //将符合周数条件的数据放入新数组中
					$all_tag++;
				}
			}
			$gathered=array_unique($gathered); 					   //去重
			$all_gathered=array_unique($all_gathered);
			$final_result=array_diff($all_gathered,$gathered);     //群体学生与有课学生取差集
			//print_r ($all_gathered);
			
			return $final_result;
			mysqli_close($db);
		}
		
?>
<?php	if(isset($_POST['thisweek'])) $thisweek=$_POST['thisweek']; else $thisweek=1; echo "第".$thisweek."周"; ?>

<form ENCTYPE="multipart/form-data" ACTION="testmethod.php" METHOD="POST">
<input type=text name="thisweek">
<input type=submit>
<table width="1800" border="1" height="800">
<tr><th></th> <th>星期一</th> <th>星期二</th> <th>星期三</th> <th>星期四</th> <th>星期五</th> <th>星期六</th><th>星期日</th></tr>

<?php $xqname=["第一二节","第三四节","第五六节","第七八节","第九十节","第十一十二节"];
for($thiskj=0;$thiskj<=5;$thiskj++)							//绘制纵行
{ ?>
	<tr>
	<td><?php echo $xqname[$thiskj] ?></td>			<!--第一纵行显示课节-->
	<!-------------输出星期------------->
	<?php for($thisxq=1;$thisxq<=7;$thisxq++)	//余下的纵行循环生成
	{?>
		<td>
		<?php
		$final_result=isFree($thisweek,$thisxq,$thiskj);
		foreach($final_result as $value){ 
				echo $value.' ';		}
		
		echo "</td>";
	} 
		echo "</tr>";
}
?>

<a href="index.php">back</a>
</body>
</html>