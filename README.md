# yayinci_abone_ornek


Workspace yok ise workspace oluşturunuz.

Örn. http://wiki.ros.org/catkin/Tutorials/create_a_workspace

Daha sonra workspace gidiniz ve paketi indiriniz.

cd <WORKSPACE_NAME>

git clone "https://github.com/inomuh/yayinci_abone_ornek.git"

cd <WORKSPACE_NAME>

catkin_make

catkin_make install

source devel/setup.bash




Yayıncı ve Aboneyi çalıştırmak için

$ roslaunch yayinci_abone_ornek yayinci_abone_ornek_baslat.launch
