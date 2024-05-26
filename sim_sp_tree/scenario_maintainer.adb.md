#sim_sp_SIM_SP_MFR_src_base
#described
[[sim_sp_SIM_SP_MFR_src_base]]

## Scenario_Maintainer package

### Description
Sets target and clutter parameters, initialize and update those objects with methods defined in scenario directory.
sector_180 methods update sectors
Deliver_Object manages all target (rcs included), clutter and sector evolutions
Update_Object former method ? (almost the same, sector clutter not updated, tests a bit different)
simulation management methods

### Methods
* Set package
* Initialize_Target
* Update_Target
* Update_Jammer_Equipment
* Initialize_Sector_Clutter
* Update_Sector_Clutter
* Initialize_Volume_Clutter
* Update_Volume_Clutter
* Remove_entity
* Sector_180_Of
* Sector_Extention_Of
* Compute_Sector_180_And_Extention
* Compute_Sector_180_Start_Stop
* Set_Sector_180_Filtering
* Initalize_Scenario
* Reset_Scenario
* Init
* Get_norm_2d
* Deliver_Object
* Update_Object
* Get_Target_Statistic



