config = {'datapath':'/kaggle/input/dsb-new/cancer_1/',
          'preprocess_result_path':'/kaggle/input/dsb-new/prep_result/',
          'outputfile':'prediction.csv',
          
          'detector_model':'net_detector.py',
         'detector_param':'/kaggle/input/dsb-new/model/detector.ckpt',
         'classifier_model':'net_classifier',
         'classifier_param':'/kaggle/input/dsb-new/model/classifier.ckpt',
         'n_gpu':1,
         'n_worker_preprocessing':None,
         'use_exsiting_preprocessing':False,
         'skip_preprocessing':True,
         'skip_detect':False}
