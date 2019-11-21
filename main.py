import extraction_module.py
import gui_module.py

main():
    # introduce this in a loop to iterate through all time codes
    time_code_map = extraction_module.main("src/sim_data_p01_s03a_nfd.csv")
    print time_code_map
    
