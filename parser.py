# -*-coding:utf-8 -*-
from struct import *
import codecs


class Parser:
    def __init__(self,name):
        self.name = name
        self.j = 0
        self.element = 0
        self.layer = 0
        self.layers = dict()

    def OpenAlt(self):
        with open(self.name, "rb") as  f:
            self.s = f.read()
            # self.s = self.s.split(b"$$HEADEREND")[1]

    def Open(self):
        with open(self.name, "rb") as  f:
            self.s = f.read()


    def scale(self,x,y):
        # x_scaled, y_scaled = int((float(x) / 65536 * 10000) / 2), int((float(y) / 65536 * 10000) / 2)
        x_scaled, y_scaled = int((float(x) / 65536 * 10000) ), int((float(y) / 65536 * 10000))
        return x_scaled,y_scaled

    def get_command111(self,s):


        c = unpack("H", s[:2])[0]

        s = s[2:]
        print(c)
        if c == 128:  # layer
            self.layer += 1
            self.layers[str(self.layer)] = list()
            print(str(self.layer) + ' layer num')
            z = unpack("H", s[:2])[0]
            s = s[2:]
            element = 0
            print("Start layer (128) %s" % z)
        elif c == 129:
            id_ = unpack("H", s[:2])
            s = s[2:]
            dir_ = unpack("H", s[:2])
            s = s[2:]
            n = unpack("H", s[:2])[0]
            s = s[2:]
            print("Start polyline (129) id: %s; dir: %s; n: %s;" % (id_, dir_, n))
            coord_list = list()
            for i in range(n):
                x, y = unpack("HH", s[:4])

                s = s[4:]
                x_scaled, y_scaled =self.scale(x,y)
                coord_list.append(x_scaled)
                coord_list.append(y_scaled)

                # print(x_scaled, y_scaled)
                print(x, y)
            print()
            self.layers[str(self.layer)].append(coord_list)
            self.element += 1

        elif  c == 131:
            id_ = unpack("H", s[:2])
            s = s[2:]
            dir_ = unpack("H", s[:2])
            s = s[2:]
            n = unpack("H", s[:2])[0]
            s = s[2:]
            print("Start hatch (131) id: %s; dir: %s; n: %s;" % (id_, dir_, n))
            coord_list = list()
            for i in range(n):
                x, y, x1,y1 = unpack("HHHH", s[:8])
                x,y = self.scale(x,y)
                x1,y1 = self.scale(x1,y1)
                s = s[8:]

                coord_list.append(x)
                coord_list.append(y)
                coord_list.append(x1)
                coord_list.append(y1)

                # print(x_scaled, y_scaled)
                print(x, y)
            print()
            self.layers[str(self.layer)].append(coord_list)
            self.element += 1
        else:
            print ("Bad command found! c = %s"%c)

            i = unpack("H", s[:2])
            s = s[2:]
            print(i) # print(i)






            return ""
        return s

    def Run(self):
        self.Open()
        while len(self.s) > 0:
            self.s = self.get_command(self.s)
        #
        # self.parced_layers = self.layers
        # print(self.layers['1'])

    def get_command(self, s):
        self.layers = {}
        s = open(s,"r").read()
        coord_list = []
        for l in s.split("\n"):
            # print (l)
            if l[:3] == "G02" :
                self.layer += 1
                # if self.layer != 0 :
                #     self.layers[str(self.layer-1)] = self.coord_list
                self.coord_list = []
                self.layers[str(self.layer)] = list()
                # print(str(self.layer) + ' layer num')
                element = 0
                # print("Start layer (128) ")

                # self.layers[str(self.layer)].append(self.coord_list)
            elif l[:3] == "M01":
                # print("M00")
                # self.element += 1
                # print("self.coord_list")
                # print(self.coord_list)
                if len(self.coord_list)>0:
                    self.layers[str(self.layer)].append(self.coord_list)
                self.coord_list = []
            elif l[:3] in ["G01","G03"] :
                x,y = l.split()[1:3]
                x,y = self.scale(x,y)
                # print(x)
                # print(y)
                self.coord_list.append(int(x))
                self.coord_list.append(int(y))



            self.parced_layers = self.layers

if __name__ == '__main__':

    # par = Parser("s_11zzz1_ex.cli")
    par = Parser("meiko_main.nc")
    # par.Run()
    par.get_command("meiko_main.nc")
    print(par.parced_layers)

