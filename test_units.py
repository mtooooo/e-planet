import os
from time import sleep as wait
from CANoe import CANoe

file_path = os.path.dirname(os.path.abspath(__file__)).replace('/', '//')

# 运行CANoe程序
application = CANoe()


def test_canoe_xxxx():
    '''message：模板函数'''
    application.open_cfg(cfgname=fr'{file_path}/demo_cfg/demo.cfg')
    wait(2)


def test_canoe_version():
    '''message：获取CANoe版本号'''
    canoe_version = application.canoe_version
    print(f'CANoe version is {canoe_version}')
    wait(2)


def test_canoe_open_and_close_cfg_project():
    '''message：加载.cfg工程, 关闭CANoe工具'''
    application.open_cfg(cfgname=fr'{file_path}/demo_cfg/demo.cfg')
    wait(5)
    application.close_cfg()
    wait(5)


def test_canoe_start_and_stop_cfg_project():
    '''message：启动和停止运行.cfg工程'''
    application.open_cfg(cfgname=fr'{file_path}/demo_cfg/demo.cfg')
    wait(5)
    application.start_measurement()
    wait(5)
    application.stop_measurement()
    wait(5)


def test_canoe_get_cfg_project_status():
    '''message：获取.cfg工程运行状态'''
    application.open_cfg(cfgname=fr'{file_path}/demo_cfg/demo.cfg')
    wait(5)
    is_running = application.get_measurement_state()
    print(f'canoe running is {is_running}')
    wait(5)
    application.stop_measurement()
    wait(5)


def test_canoe_capl_function():
    '''message：调用capl函数示例'''
    application.open_cfg(cfgname=fr'{file_path}/demo_cfg/demo.cfg')
    wait(2)


def test_canoe_get_signal_value():
    '''message：获取信号值(物理值)'''
    application.open_cfg(cfgname=fr'{file_path}/demo_cfg/demo.cfg')
    wait(5)
    application.start_measurement()
    wait(5)
    value = application.get_signal_value(channel_num=1, msg_name='EngineState',
                                       sig_name='EngineSpeed', bus_type='CAN')
    print(f'signal value is {value}')
    wait(5)
    application.stop_measurement()


def test_canoe_get_raw_signal_value():
    '''message：获取信号值(真实值)'''
    application.open_cfg(cfgname=fr'{file_path}/demo_cfg/demo.cfg')
    wait(5)
    application.start_measurement()
    wait(5)
    value = application.get_raw_signal_value(channel_num=1, msg_name='EngineState',
                                           sig_name='EngineSpeed', bus_type='CAN')
    print(f'raw signal value is {value}')
    wait(5)
    application.stop_measurement()


def test_canoe_set_signal_value():
    '''message：设置信号值'''
    application.open_cfg(cfgname=fr'{file_path}/demo_cfg/demo.cfg')
    wait(5)
    application.start_measurement()
    wait(5)
    application.set_signal_value(channel_num=1, msg_name='EngineState',
                                sig_name='EngineSpeed', bus_type='CAN', setValue=2000)
    wait(5)
    application.stop_measurement()


def test_canoe_read_or_write_window():
    '''message：在Write窗口读取和写入信息'''
    application.open_cfg(cfgname=fr'{file_path}/demo_cfg/demo.cfg')
    wait(5)
    application.start_measurement()
    wait(5)
    application.write_text_in_write_window(text='hello canoe from python!')
    wait(5)
    text = application.read_text_from_write_window()
    print(f'canoe Write窗口读取到的信息为：{text}')
    wait(5)
    application.stop_measurement()


def test_canoe_clear_write_window():
    '''message：清空Write窗口信息'''
    application.open_cfg(cfgname=fr'{file_path}/demo_cfg/demo.cfg')
    wait(5)
    application.start_measurement()
    wait(5)
    application.clear_write_window_content()
    wait(5)
    application.stop_measurement()


def test_canoe_write_window_output_file():
    '''message：保存Write窗口信息到本地文件'''
    application.open_cfg(cfgname=fr'{file_path}/demo_cfg/demo.cfg')
    wait(5)
    application.start_measurement()
    wait(5)
    output_file = './canoe_write_window.log'  # 相对路径为.cfg文件的相对路径
    application.enable_write_window_output_file(output_file=output_file)
    wait(5)
    application.stop_measurement()


def test_canoe_new_cfg_project():
    '''message：新建CANoe .cfg工程'''
    application.new(auto_save=True)
    wait(5)


def test_canoe_save_configuration_as():
    '''message：保存.cfg工程到其他CANoe 版本'''
    application.open_cfg(cfgname=fr'{file_path}/demo_cfg/demo.cfg')
    wait(5)
    # 保存CANoe工程到14 0版本
    application.save_configuration_as(path=fr'{file_path}/demo_v14.cfg', major=14, minor=0)
    wait(5)


def test_canoe_check_signal_online():
    '''message：检查信号是否在线'''
    application.open_cfg(cfgname=fr'{file_path}/demo_cfg/demo.cfg')
    wait(5)
    application.start_measurement()
    wait(5)
    is_online = application.check_signal_online(bus='CAN', channel=1, message='LightState', signal='FlashLight')
    print(f'signal online is {is_online}')
    wait(5)
    application.stop_measurement()


def test_canoe_set_log_config():
    '''message：设置write窗口log信息的存储路径及格式
    写的模式是追加写,CANoe Write窗口加载一行,写一行
    '''
    # 方式一：不设置保存路径和格式,默认存储在D://vector_log文件夹中,名称为[年月日_时_分.log]
    application.open_cfg(cfgname=fr'{file_path}/demo_cfg/demo.cfg')
    wait(5)
    application.set_log_config()
    application.start_measurement()
    wait(5)
    application.write_text_in_write_window('hello world python!')
    application.stop_measurement()
    wait(5)

    # 方式二：相对路径存储log,使用相对路径导出的log文件是在.cfg的相对路径下
    application.open_cfg(cfgname=fr'{file_path}/demo_cfg/demo.cfg')
    wait(5)
    application.set_log_config('./', 'write_output_test.log')
    application.start_measurement()
    wait(5)
    application.write_text_in_write_window('hello world python!')
    application.stop_measurement()
    wait(5)

    # 方式三：绝对路径存储log
    application.open_cfg(cfgname=fr'{file_path}/demo_cfg/demo.cfg')
    wait(5)
    # 绝对路径可以是正斜杠也可以是反斜杠是D://xxx或D://xxx或 r'D:/xxx'
    # 绝对路径结尾可以加//也可以不加
    application.set_log_config(r'D://vector_log//', 'write_output_test.log')
    application.start_measurement()
    wait(5)
    application.write_text_in_write_window('hello world python!')
    application.stop_measurement()
    wait(5)


def test_canoe_disable_write_window_output_file():
    '''message：设置write窗口log信息不保存到本地文件中'''
    application.open_cfg(cfgname=fr'{file_path}/demo_cfg/demo.cfg')
    wait(5)
    application.set_log_config(r'D:/vector_log', 'write_output_test_new.log')  # 先创建一个保存的文件
    wait(5)
    application.disable_write_window_output_file()  # 测试CANoe Write窗口的log信息没有导出到文件中
    application.start_measurement()
    wait(5)
    application.write_text_in_write_window('hello world python!')
    application.stop_measurement()
    wait(5)


def test_canoe_get_can_bus_statistics():
    '''message：根据CAN总线通道获取该总线的统计数据'''
    application.open_cfg(cfgname=fr'{file_path}/demo_cfg/demo.cfg')
    application.get_can_bus_statistics(channel=1)  # 程序开始运行前获取channel 1内容
    wait(5)
    application.start_measurement()
    wait(5)
    application.get_can_bus_statistics(channel=1)  # 程序运行过程中,获取channel 1内容
    wait(5)
    application.get_can_bus_statistics(channel=1)  # 程序运行过程中,获取channel 1 内容
    application.stop_measurement()
    wait(5)


def test_canoe_get_networks():
    '''message：获取CAN、LIN、ETH等网络节点列表'''
    application.open_cfg(cfgname=fr'{file_path}/demo_cfg/demo.cfg')
    result = application.get_networks()
    print(result)


def test_canoe_get_ecus():
    '''message：根据通道查询ecu列表'''
    application.open_cfg(cfgname=fr'{file_path}/demo_cfg/demo.cfg')
    result = application.get_ecus(channel_name='CAN1')
    print(result)


def test_canoe_il_node_control_start_and_stop():
    '''message：打开或关闭ECU节点'''
    # .cfg工程需要在未运行模式
    application.open_cfg(cfgname=fr'{file_path}/demo_cfg/demo.cfg')
    application.il_node_control_stop(network_name='CAN1', node_name='Light')
    wait(10)
    application.il_node_control_start(network_name='CAN1', node_name='Light')


def test_canoe_capl_function():
    '''message：python调用capl函数示例'''
    application.open_cfg(cfgname=fr'{file_path}/demo_cfg/demo.cfg')
    application.start_measurement()
    wait(5)
    application.capl_function(num1=12, num2=13)
    wait(5)
    application.stop_measurement()
    wait(5)


def test_canoe_test_module_load():
    '''message：加载test module'''
    application.open_cfg(cfgname=fr'{file_path}/demo_cfg/demo.cfg')
    application.start_measurement()
    wait(5)
    application.test_module_load('1')
    wait(5)
    application.stop_measurement()
    wait(5)


def test_canoe_send_diag_request():
    '''message：诊断测试仪（客户端）向CANoe中的ECU（服务器）查询'''
    # 方式一：
    application.open_cfg(cfgname=fr'{file_path}/demo_cfg/demo.cfg')
    application.start_measurement()
    wait(20)
    resp = application.send_diag_request('Door', '10 01')
    print(resp)
    wait(5)
    application.stop_measurement()
    wait(5)
    # 方式二：
    application.start_measurement()
    wait(20)
    resp = application.send_diag_request('Door', 'DefaultSession_Start', False)
    print(resp)
    wait(5)
    application.stop_measurement()
    wait(5)


def test_canoe_set_replay_block_file():
    '''message：设置CANoe重放块文件'''
    # application.open_cfg(cfgname=fr'{file_path}/demo_cfg/demo.cfg')
    wait(5)
    application.set_replay_block_file(block_name=r'Trace',
                                    recording_file_path=r'D:/GITEE/ling-shu/CANoeCOMserver/AA打包pyd/source/demo_cfg/Trace.blf')
    wait(5)
    application.start_measurement()
    wait(5)
    application.stop_measurement()
    wait(5)


def test_canoe_save_trace_config():
    '''message:CANoe trace保存路径和格式设置'''
    # 方式一：不设置保存路径和参数,默认存储在D://vector_log文件夹中名称名称为[年月日_时_分.asc]
    application.open_cfg(cfgname=fr'{file_path}/demo_cfg/demo.cfg')
    application.save_trace_config()
    wait(5)
    application.start_measurement()
    wait(5)
    application.stop_measurement()
    wait(20)

    # 方式二：相对存储路径,是相对于CANoe工程.cfg文件的路径
    application.open_cfg(cfgname=fr'{file_path}/demo_cfg/demo.cfg')
    application.save_trace_config(trace_path=r'./', trace_name='1.blf')
    wait(5)
    application.start_measurement()
    wait(5)
    application.stop_measurement()
    wait(20)

    # 方式三：绝对存储路径
    application.open_cfg(cfgname=fr'{file_path}/demo_cfg/demo.cfg')
    application.save_trace_config(trace_path=r'D:/vector_log', trace_name='1.pcap')
    wait(5)
    application.start_measurement()
    wait(5)
    application.stop_measurement()
    wait(5)


def test_canoe_get_and_set_system_variable_value():
    '''message:获取设置系统变量值、和设置系统变量值'''
    application.open_cfg(cfgname=fr'{file_path}/demo_cfg/demo.cfg')
    wait(10)
    application.start_measurement()
    wait(10)
    sys_var1 = application.get_system_variable_value(sys_var_name='ept_com_api_system_variables::sys_var1')
    print(f'修改前：sys_var1(Type Int32) value is {sys_var1}')
    wait(5)
    application.set_system_variable_value(sys_var_name='ept_com_api_system_variables::sys_var1', value=20)
    wait(5)
    sys_var1 = application.get_system_variable_value(sys_var_name='ept_com_api_system_variables::sys_var1')
    print(f'修改后：sys_var1(Type Int32) value is {sys_var1}')
    # 对于Int Array的数据类型需要传tuple类型,且tuple的元素需要是int类型,长度要和原先一致
    wait(5)
    application.set_system_variable_value(sys_var_name='ept_com_api_system_variables::sys_var2',
                                        value=(8, 7, 6, 5, 4, 3, 2, 1))
    wait(5)
    sys_var2 = application.get_system_variable_value(sys_var_name='ept_com_api_system_variables::sys_var2')
    print(f'sys_var2(Type Int32 Array) value is {sys_var2}')
    # 对于Double Array的数据类型需要传tuple类型,且tuple的元素需要是float类型,长度要和原先一致
    wait(5)
    application.set_system_variable_value(sys_var_name='ept_com_api_system_variables::sys_var3',
                                        value=(6.0, 5.0, 4.0, 3.0, 2.0, 1.0))
    wait(5)
    sys_var3 = application.get_system_variable_value(sys_var_name='ept_com_api_system_variables::sys_var3')
    print(f'sys_var3(Type Double Array) value is {sys_var3}')
    wait(5)
    application.set_system_variable_value(sys_var_name='ept_com_api_system_variables::sys_var4', value='HelloWorld!')
    wait(5)
    sys_var4 = application.get_system_variable_value(sys_var_name='ept_com_api_system_variables::sys_var4')
    print(f'sys_var4(Type String) value is {sys_var4}')
    wait(5)
    application.stop_measurement()
    wait(10)


def test_canoe_send_can_message():
    '''message：发送CAN信号'''
    application.open_cfg(cfgname=fr'{file_path}/demo_cfg/demo.cfg')
    wait(5)
    application.start_measurement()
    wait(5)
    # demo工程只有CAN frame没有CAN fd所以没办法发送超过8位的数据
    application.send_can_message(channel=1, can_id=0x101, data=[1, 2, 3, 4])
    wait(5)
    application.send_can_message(channel=1, can_id=0x102, data=[5, 4, 3, 2, 1])
    wait(5)
    application.stop_measurement()
    wait(5)


def test_canoe_send_can_message_loop():
    '''message：周期发送CAN信号'''
    application.open_cfg(cfgname=fr'{file_path}/demo_cfg/demo.cfg')
    wait(5)
    application.start_measurement()
    wait(5)
    application.send_can_message_loop(channel=1, can_id=0x103, data=[1, 2, 3, 4], cycles=100)
    wait(5)
    application.send_can_message_loop(channel=1, can_id=0x104, data=[5, 4, 3, 2, 1], cycles=20)
    wait(5)
    application.stop_measurement()
    wait(5)


def test_canoe_stop_send_can_message():
    '''message：停止周期发送CAN信号'''
    application.open_cfg(cfgname=fr'{file_path}/demo_cfg/demo.cfg')
    wait(5)
    application.start_measurement()
    wait(5)
    application.send_can_message_loop(channel=1, can_id=0x105, data=[1, 2, 3, 4, 5], cycles=200)
    wait(5)
    application.stop_send_can_message(channel=1, can_id=0x105)
    wait(20)
    application.stop_measurement()
    wait(5)


def test_canoe_send_and_stop_can_message_secret():
    '''message：1.周期发送CAN信号+校验算法2.停止校验算法发送CAN报文'''
    application.open_cfg(cfgname=fr'{file_path}/demo_cfg/demo.cfg')
    wait(5)
    application.start_measurement()
    wait(5)
    application.send_can_message_secret(channel=1, can_id=0x103, data=[1, 2, 3, 4], cycles=100, secret='CRC8')
    wait(5)
    application.stop_send_can_message_secret(channel=1, can_id=0x103)
    wait(5)
    application.send_can_message_secret(channel=1, can_id=0x104, data=[5, 4, 3, 2, 1], cycles=20, secret='CRC16')
    wait(20)
    application.stop_measurement()
    wait(5)


if __name__ == '__main__':
    # test_canoe_version()
    # test_canoe_open_and_close_cfg_project()
    # test_canoe_start_and_stop_cfg_project()
    # test_canoe_get_cfg_project_status()
    # test_canoe_get_signal_value()
    # test_canoe_get_raw_signal_value()
    # test_canoe_set_signal_value()
    # test_canoe_read_or_write_window()
    # test_canoe_clear_write_window()
    # test_canoe_write_window_output_file()
    # test_canoe_new_cfg_project()
    # test_canoe_save_configuration_as()
    # test_canoe_check_signal_online()
    # test_canoe_set_log_config()
    # test_canoe_disable_write_window_output_file()
    # test_canoe_get_can_bus_statistics()
    # test_canoe_get_networks()
    # test_canoe_il_node_control_start_and_stop()
    # test_canoe_get_ecus()
    # test_canoe_capl_function()
    # test_canoe_test_module_load()
    # test_canoe_send_diag_request()
    # test_canoe_set_replay_block_file()
    # test_canoe_save_trace_config()
    # test_canoe_get_and_set_system_variable_value()
    # test_canoe_send_can_message()
    # test_canoe_send_can_message_loop()
    # test_canoe_stop_send_can_message()
    # test_canoe_send_and_stop_can_message_secret()
    pass

