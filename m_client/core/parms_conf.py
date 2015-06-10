

params = {'get_configuration': '/api/configuration/1/?format=json',
          'post_monitor_data': '/api/monitor_data/',
          'get_asset_id': '/api/asset/',
          'config_md5': None,
          'server': '10.168.66.23',
          'port':80,
          
          
          #########below for task allocation########
          
          'get_host_profile': '/api/host_profile/1/?format=json',
          'new_tasks': '/api/new_tasks',
          'report_result': '/api/task_result/',
          'task_log_path':'logs/tasks',
          'last_task_id' : 'var/last_task_id',
          }
