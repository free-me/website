;!function(){

//增加和修改弹窗-资产
$('.boxdemo1').on('click', function(){
	layer.open({
	  btn: ['提交','取消'], //按钮
	  type: 2,
	  closeBtn: 1,
	  skin: 'layui-layer-rim', //加上边框
	  title: '新增/修改资产',
	  shadeClose: true,
	  area: ['600px', '500px'],
	  maxmin: true, //开启最大化最小化按钮
	  anim: 2,
	  content: ['././form_modal_add_zichan.html', 'yes'], //iframe的url，no代表不显示滚动条
	});
});

//删除弹窗-资产
$('.boxdemo2').on('click', function(){
	layer.confirm('删除后数据无法恢复，是否仍要删除“名称”资产？', {
	  btn: ['确定','取消'] //按钮
	}, function(){
	  layer.msg('删除成功', {icon: 1});
	}, function(){
	  layer.msg('取消删除', {icon: 2});
	});
});

//导入文件
$('.boxdemo3').on('click', function(){
	layer.open({
	  btn: ['提交','取消'], //按钮
	  type: 2,
	  closeBtn: 1,
	  skin: 'layui-layer-rim', //加上边框
	  title: '导入文件',
	  shadeClose: true,
	  area: ['500px', '260px'],
	  maxmin: true, //开启最大化最小化按钮
	  anim: 2,
	  content: ['././form_modal_upload.html', 'yes'], //iframe的url，no代表不显示滚动条
	});
});


//增加和修改弹窗-系统
$('.boxdemo4').on('click', function(){
	layer.open({
	  btn: ['提交','取消'], //按钮
	  type: 2,
	  closeBtn: 1,
	  skin: 'layui-layer-rim', //加上边框
	  title: '新增/修改业务系统',
	  shadeClose: true,
	  area: ['600px', '550px'],
	  maxmin: true, //开启最大化最小化按钮
	  anim: 2,
	  content: ['././form_modal_add_xitong.html', 'yes'], //iframe的url，no代表不显示滚动条
	});
});

$('.boxdemo4_1').on('click', function(){
	layer.open({
	  btn: ['提交','取消'], //按钮
	  type: 2,
	  closeBtn: 1,
	  skin: 'layui-layer-rim', //加上边框
	  title: '新增/修改设备类型',
	  shadeClose: true,
	  area: ['600px', '340px'],
	  maxmin: true, //开启最大化最小化按钮
	  anim: 2,
	  content: ['././form_modal_add_shebei.html', 'yes'], //iframe的url，no代表不显示滚动条
	});
});

$('.boxdemo4_2').on('click', function(){
	layer.open({
	  btn: ['提交','取消'], //按钮
	  type: 2,
	  closeBtn: 1,
	  skin: 'layui-layer-rim', //加上边框
	  title: '新增/修改操作系统类型',
	  shadeClose: true,
	  area: ['600px', '340px'],
	  maxmin: true, //开启最大化最小化按钮
	  anim: 2,
	  content: ['././form_modal_add_shuxing.html', 'yes'], //iframe的url，no代表不显示滚动条
	});
});

//删除弹窗-系统
$('.boxdemo5').on('click', function(){
	layer.confirm('删除后数据无法恢复，是否仍要删除“业务系统名称”的业务系统名称？', {
	  btn: ['确定','取消'] //按钮
	}, function(){
	  layer.msg('删除成功', {icon: 1});
	}, function(){
	  layer.msg('取消删除', {icon: 2});
	});
});

//删除弹窗-系统
$('.boxdemo5_1').on('click', function(){
	layer.confirm('确认删除“设备类型名称”的设备类型？', {
	  btn: ['确定','取消'] //按钮
	}, function(){
	  layer.msg('删除成功', {icon: 1});
	}, function(){
	  layer.msg('取消删除', {icon: 2});
	});
});

//删除弹窗-系统
$('.boxdemo5_2').on('click', function(){
	layer.confirm('确认删除“操作系统类型名称”的操作系统类型？', {
	  btn: ['确定','取消'] //按钮
	}, function(){
	  layer.msg('删除成功', {icon: 1});
	}, function(){
	  layer.msg('取消删除', {icon: 2});
	});
});


//增加和修改弹窗-发布
$('.boxdemo6').on('click', function(){
	layer.open({
	  btn: ['提交','取消'], //按钮
	  type: 2,
	  closeBtn: 1,
	  skin: 'layui-layer-rim', //加上边框
	  title: '新增/修改业务系统',
	  shadeClose: true,
	  area: ['600px', '550px'],
	  maxmin: true, //开启最大化最小化按钮
	  anim: 2,
	  content: ['././form_modal_add_fabu.html', 'yes'], //iframe的url，no代表不显示滚动条
	});
});

$('.boxdemo7').on('click', function(){
	layer.open({
	  btn: ['提交','取消'], //按钮
	  type: 2,
	  closeBtn: 1,
	  skin: 'layui-layer-rim', //加上边框
	  title: '新增/修改扫描任务',
	  shadeClose: true,
	  area: ['600px', '550px'],
	  maxmin: true, //开启最大化最小化按钮
	  anim: 2,
	  content: ['././form_modal_add_renwu.html', 'yes'], //iframe的url，no代表不显示滚动条
	});
});

$('.boxdemo8').on('click', function(){
	layer.open({
	  btn: ['提交','取消'], //按钮
	  type: 2,
	  closeBtn: 1,
	  skin: 'layui-layer-rim', //加上边框
	  title: '新增/修改扫描引擎',
	  shadeClose: true,
	  area: ['600px', '500px'],
	  maxmin: true, //开启最大化最小化按钮
	  anim: 2,
	  content: ['././form_modal_add_yinqing.html', 'yes'], //iframe的url，no代表不显示滚动条
	});
});

//删除弹窗-发布
$('.boxdemo9').on('click', function(){
	layer.confirm('确认删除“漏洞标题”的发布漏洞?', {
	  btn: ['确定','取消'] //按钮
	}, function(){
	  layer.msg('删除成功', {icon: 1});
	}, function(){
	  layer.msg('取消删除', {icon: 2});
	});
});

$('.boxdemo10').on('click', function(){
	layer.confirm('确认删除“任务名称”的扫描任务?', {
	  btn: ['确定','取消'] //按钮
	}, function(){
	  layer.msg('删除成功', {icon: 1});
	}, function(){
	  layer.msg('取消删除', {icon: 2});
	});
});

$('.boxdemo11').on('click', function(){
	layer.confirm('确认删除“扫描引擎名称”的扫描引擎?', {
	  btn: ['确定','取消'] //按钮
	}, function(){
	  layer.msg('删除成功', {icon: 1});
	}, function(){
	  layer.msg('取消删除', {icon: 2});
	});
});


$('.boxdemo12').on('click', function(){
	layer.open({
	  btn: ['提交','取消'], //按钮
	  type: 2,
	  closeBtn: 1,
	  skin: 'layui-layer-rim', //加上边框
	  title: '新增/修改用户',
	  shadeClose: true,
	  area: ['600px', '500px'],
	  maxmin: true, //开启最大化最小化按钮
	  anim: 2,
	  content: ['././form_modal_add_yonghu.html', 'yes'], //iframe的url，no代表不显示滚动条
	});
});


$('.boxdemo13').on('click', function(){
	layer.confirm('确认删除“用户名”的用户?', {
	  btn: ['确定','取消'] //按钮
	}, function(){
	  layer.msg('删除成功', {icon: 1});
	}, function(){
	  layer.msg('取消删除', {icon: 2});
	});
});


$('.boxdemo14').on('click', function(){
	layer.open({
	  btn: ['提交','取消'], //按钮
	  type: 2,
	  closeBtn: 1,
	  skin: 'layui-layer-rim', //加上边框
	  title: '新增/修改用户组',
	  shadeClose: true,
	  area: ['600px', '350px'],
	  maxmin: true, //开启最大化最小化按钮
	  anim: 2,
	  content: ['././form_modal_add_yonghuzu.html', 'yes'], //iframe的url，no代表不显示滚动条
	});
});



$('.boxdemo15').on('click', function(){
	layer.confirm('确认删除“用户组名称”的用户组?', {
	  btn: ['确定','取消'] //按钮
	}, function(){
	  layer.msg('删除成功', {icon: 1});
	}, function(){
	  layer.msg('取消删除', {icon: 2});
	});
});






}();