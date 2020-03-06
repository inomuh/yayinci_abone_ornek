#!/usr/bin/env python
# coding=utf-8

import rospy

from std_msgs.msg import Float32
import random

class AboneOrnek(object):
    def __init__(self):

        self.ana_fonksiyon()


    def ana_fonksiyon(self):
        # /mesafe_hesabi_ornek topiğine abone olmaktadır.
        # MesafeBilgisiOrnek msg üzerinden mesajlaşmayı sağlamaktadır.
        # self.mesafe_hesabi_callback_fonksiyonu topikten gelen değerleri okumak ve işlem yapmak için çağırılan fonksiyondur.
        rospy.Subscriber('/mesafe_hesabi_ornek', Float32, self.mesafe_hesabi_callback_fonksiyonu)

        rospy.spin()


    def mesafe_hesabi_callback_fonksiyonu(self, okunan_mesafe_bilgisi_mesaji):
        # mesafe_bilgisi_mesaji mesajinın içeriğini okur.
        print("\nOkunan deger = " + str(okunan_mesafe_bilgisi_mesaji.data) + "\n\n\n")


if __name__ == '__main__':
    try:
        rospy.init_node('abone_ornek_dugumu', anonymous=True)

        # AboneOrnek() sınıfını çağırmaktadır.
        dugum = AboneOrnek()

    except rospy.ROSInterruptException:
        pass
