# Coral Reefs Management System
This program consists of two role, the Manager  and the Inspector. The Manager's menu includes features to Show Corals Data, Update Corals Data, Delete Corals Data, Update Corals Data, Back to the Login Page, and Exit the Program. On the other hand, the Inspector's menu offers features to Show Corals Data, Inspection (Add Corals to be Checked), Show Still Maintained Corals, Complete the Maintained Corals, Back to the Login Page, and Exit the Program.

## Background Story
Coral Reefs, or also can be called as Ocean rainforest, although only has a population of approximately 0.01% but is able to protect about 25% of all life in the sea from various species of fish and other invertebrate creatures [<sup>[1]</sup>](https://education.nationalgeographic.org/resource/coral-reefs/#:~:text=Reefs%20provide%20a%20large%20fraction%20of%20Earth%E2%80%99s%20biodiversity%E2%80%94they%20have%20been%20called%20%E2%80%9Cthe%20rain%20forests%20of%20the%20seas.%E2%80%9D%20Scientists%20estimate%20that%2025%20percent%20of%20all%20marine%20species%20live%20in%20and%20around%20coral%20reefs%2C%20making%20them%20one%20of%20the%20most%20diverse%20habitats%20in%20the%20world.)[<sup>[2]</sup>](https://coral.org/en/coral-reefs-101/#:~:text=Although%20they%20cover%20less%20than%200.1%25%20of%20the%20earth%E2%80%99s%20surface%2C%20coral%20reefs%20are%20the%20most%20biodiverse%20marine%20ecosystem%20in%20the%20world.). In addition, this ecosystem is very useful in protecting the shoreline [<sup>[3]</sup>](https://resourcewatch.org/dashboards/coral-reefs#:~:text=Reefs%20protect%20an%20estimated%20150%2C000%20km%20of%20shoreline%20in%20more%20than%20100%20countries%20and%20territories.%C2%A0On%20average%2C%20coral%20reefs%20reduce%20the%20annual%20expected%20damages%20from%20storms%20globally%20by%20more%20than%20US%244%20billion.), supporting the community's economy especially in tourist areas [<sup>[2]</sup>](https://coral.org/en/coral-reefs-101/#:~:text=Over%20100%20countries%20benefit%20from%20the%20recreational%20value%20of%20coral%20reefs)[<sup>[3]</sup>](https://resourcewatch.org/dashboards/coral-reefs#:~:text=Coral%20reefs%20are%20an%20important%20magnet%20for%20both%20domestic%20and%20international%20tourism%20in%20over%20100%20countries%20and%20territories%2C%20generating%20jobs%2C%20revenue%20and%20foreign%20exchange.), and even could be used as secrets source of medicine in the future. The Coral Reefs that located in Raja Ampat (Indonesia) according to the Goldman Environmental Prize winner, are the healthiest compared to Coral Reefs in other regions (which experiencing vulnerability and bleaching) [<sup>[4]</sup>](https://www.goldmanprize.org/blog/protecting-the-remarkable-coral-reefs-of-raja-ampat-indonesia/#:~:text=Zafer%20is%20optimistic,in%20other%20places.). Jump back in 2022 the UN Biodiversity Convention parties said that by 2030, around 30% of the world's terrestrial, inland water, coastal, and marine areas must be in effective protection and management [<sup>[4]</sup>](https://www.goldmanprize.org/blog/protecting-the-remarkable-coral-reefs-of-raja-ampat-indonesia/#:~:text=Indeed%2C%20in%202022%20the%20parties%20to%20the%20UN%20Biodiversity%20Convention%20called%20for%2030%25%20of%20the%20world%E2%80%99s%20terrestrial%2C%20inland%20water%2C%20coastal%2C%20and%20marine%20areas%20to%20be%20in%20effective%20protection%20and%20management%20by%202030%20(emphasis%20added)). Therefore, in order to maintain, monitor, and improve continuously of the Coral Reefs especially in Raja Ampat (Indonesia), which then serve as the best example worldwide, need to be digitized seamlessly with this Coral Reefs Management System Program made using Python.

<sub><small>1. National Geographic</small></sub><br>
<sub><small>2. Coral.org 101</small></sub><br>
<sub><small>3. Resourcewatch</small></sub><br>
<sub><small>4. Goldmanprize.org</small></sub>

## How to Run
1. Make sure Python 3.8+ installed on your Computer.
2. Clone or download this Repository locally (on your own Computer Machine).
3. On Command Prompt/Powershell (Windows), Terminal (Mac/Linux). Do either `pip install tabulate maskpass` or `conda install tabulate maskpass` on your System of Global Environment (you could also do it inside a Virtual Environment). <br>
    3.1. tabulate=0.9.0 (or up) <br>
    3.2. maskpass=0.3.7 (or up)
4. Run the *corals_main_program.py* on terminal (in the same directory just write `python corals_main_program.py` and enter).
5. Enjoy the program.

[*Password File*](https://github.com/zeenfts/coral-reefs-management-system/blob/main/files/__password_role.txt)

## Limitations:
1. No Graphical User Interfaces (GUI).
2. Can only finish all of current maintained corals.
3. Only one user available for each role.
4. Can only search based on the coral's name column.
5. Not using external data storage such as database.

## Program Flow
### [PDF Version](https://github.com/zeenfts/coral-reefs-management-system/blob/main/files/__password_role.txt)
### 1. Login Page to Main Menu
![Manager Login](https://github.com/zeenfts/coral-reefs-management-system/blob/main/images/flows_program/01_manager_login_menu_flow.png?raw=true)
![Inspector Login](https://github.com/zeenfts/coral-reefs-management-system/blob/main/images/flows_program/01_inspector_login_menu_flow.png?raw=true)
### 2. Read Menu (Manager & Inspector)
![Show Corals Choices](https://github.com/zeenfts/coral-reefs-management-system/blob/main/images/flows_program/02_show_corals_choices.png?raw=true)
![Show Corals Default & Ordered](https://github.com/zeenfts/coral-reefs-management-system/blob/main/images/flows_program/02_show_corals_default_ordered.png?raw=true)
![Show Filtered Column](https://github.com/zeenfts/coral-reefs-management-system/blob/main/images/flows_program/02_show_filtered_coral_column.png?raw=true)
![Searched Coral Name](https://github.com/zeenfts/coral-reefs-management-system/blob/main/images/flows_program/02_show_searched_coral_name.png?raw=true)
![Show Still Maintained Coral by Inspector](https://github.com/zeenfts/coral-reefs-management-system/blob/main/images/flows_program/07_still_being_maintained_corals_menu_inspector.png?raw=true)
### 3. Create Menu (Manager & Inspector)
![Create by Manager](https://github.com/zeenfts/coral-reefs-management-system/blob/main/images/flows_program/03_add_coral_menu_manager.png?raw=true)
![Create by Inspector Inspect Feature](https://github.com/zeenfts/coral-reefs-management-system/blob/main/images/flows_program/06_coral_check_menu_inspector.png?raw=true)
### 4. Update Menu (Manager & Inspector)
![Update Coral by Manager](https://github.com/zeenfts/coral-reefs-management-system/blob/main/images/flows_program/05_update_coral_menu_manager.png?raw=true)
![Finish Maintained Coral by Inspector](https://github.com/zeenfts/coral-reefs-management-system/blob/main/images/flows_program/08_finish_maintained_coral_inspector.png?raw=true)
### 5. Delete Menu (Manager)
![Delete Coral from Dictionary by Manager](https://github.com/zeenfts/coral-reefs-management-system/blob/main/images/flows_program/04_delete_coral_menu_manager.png?raw=true)
## Results View
### 1. Login Page View and each Role Menu
![Login Page View](https://github.com/zeenfts/coral-reefs-management-system/blob/main/images/views_program/01_login_view.png?raw=true)
![Manager Menu View](https://github.com/zeenfts/coral-reefs-management-system/blob/main/images/views_program/01_manager_menu_view.png?raw=true)
![Inspector Menu View](https://github.com/zeenfts/coral-reefs-management-system/blob/main/images/views_program/01_inspector_menu_view.png?raw=true)
### 2. Read Menu View (Manager & Inspector)
![Show Corals Choice View](https://github.com/zeenfts/coral-reefs-management-system/blob/main/images/views_program/02_display_coral_choice_view.png?raw=true)
![Show Still Maintained Coral by Inspector View](https://github.com/zeenfts/coral-reefs-management-system/blob/main/images/views_program/07_coral_still_being_maintained_inspector_view.png?raw=true)
### 3. Create Menu View (Manager & Inspector)
![Add Coral by Manager View](https://github.com/zeenfts/coral-reefs-management-system/blob/main/images/views_program/03_add_coral_manager_view.png?raw=true)
![Add want to be Maintained by Inspector View](https://github.com/zeenfts/coral-reefs-management-system/blob/main/images/views_program/06_coral_check_maintain_inspector_view.png?raw=true)
### 4. Update Menu View (Manager & Inspector)
![Update Coral by Manager View](https://github.com/zeenfts/coral-reefs-management-system/blob/main/images/views_program/05_update_coral_manager_view.png?raw=true)
![Finish Maintained Coral by Inspector View](https://github.com/zeenfts/coral-reefs-management-system/blob/main/images/views_program/08_finish_coral_maintained_inspector_view.png?raw=true)
### 5. Delete Menu View (Manager)
![Delete Coral from Dictionary by Manager View](https://github.com/zeenfts/coral-reefs-management-system/blob/main/images/views_program/04_delete_coral_manager_view.png?raw=true)
