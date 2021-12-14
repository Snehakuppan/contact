class contactdetails:
    def __init__(self,name,no,groups,emailid):
        self.name=name
        self.no=no
        self.emailid=emailid
        self.group=groups
    def opencontact(self):
        print("contact app is opened")
    def namedetail(self):
        if type(self.name)==str:
            print("name is verified")
        else:
            raise TypeError("name should contain letters alone")
            
        #phonenumberlist["name"]=entername
    def phonenumber(self):
        
        #enternumber=input("enter the number")
        
        
        if type(self.no)==str:
            print("correct type ")
        else:
            raise TypeError("no should be a str datatype")
        if len(self.no)==10:
            if (self.no[0])==9 or (self.no[0])==8 or (self.no[0])==7 or (self.no[0])==6:
                print("valid no")
            else:
                print("invalid no")
        else:
            raise ValueError("enter valid no")
    def groups(self):
        if type(self.group)==str:
            print("group verified")
        else:
            raise TypeError(" str type only")
        print("group types are family,friends,colleagues")
        if self.group =="family":
            print("group verified")
        elif self.group =="friends":
            print("group verified")
        elif self.group=="colleagues":
            print("group verified")
        else:
            print("invalid group ")
        
        
        
    
        
        
        
    def emailidverify(self):
        #entermailid=input("enter the mailid")
        if type(self.emailid)==str:
            print("correct type")
        else:
            raise TypeError("mail id should be string")
        domain="@gmail.com"
        domain1="@disys.com"
        if (self.emailid[len(self.emailid)-len(domain)]==domain or self.emailid[len(self.emailid)-len(domain1)]==domain1):
            
            print("mail is verified")
        else:
            print("enter correct mail")
           
ret=contactdetails("sneha","9123529686","family","sneha@gmail.com")
ret.opencontact()


ret.namedetail()

ret.phonenumber()

ret.groups()

ret.emailidverify()

phonenumberlist=[{"name":"amma","no":9940249686,"emailid":"sneha@gmail.com","groups":"friends"},{"name":"amritha","no":6379098872,"emailid":"amritha@gmail.com","groups":"family"},
                                {"name":"Anu","no":9445861900,"emailid":"anu@gmail.com","groups":"colleagues"},{"name":"avinash","no":9384644269,"emailid":"avinash@disys.com","groups":"family"},
                                {"name":"babytrisha","no":7338828373,"emailid":"babytrisha@gmail.com","groups":"family"},{"name":"bharath","no":9884412975,"emailid":"bharath@gmail.com","groups":"family"},
                                {"name":"bharathi","no":9940169896,"emailid":"bharathi","groups":"family"},{"name":"bathraa","no":9629247229,"emailid":"bhatra@disys","groups":"friends"},
                                {"name":"bavana","no":7299903042,"emailid":"bavana@disys.com","groups":"friends"},{"name":"benazer","no":7010656843,"emailid":"benazer@gmail.com","groups":"family"},
                                {"name":"charu","no":7358191883,"emailid":"charu@gmail.com","groups":"family"},{"name":"dad","no":9940507735,"emailid":"kuppan@disys.com","groups":"frieds"},
                                {"name":"deepthi","no":9790823577,"emailid":"deepthi@gmail.com","groups":"family"},{"name":"dhanvarshini","no":8056267526,"emailid":"dhanvarshini@gmail.com","groups":"family"},
                                {"name":"dineshdisys","no":883892482,"emailid":"dinesh@disys.com","groups":"family"},{"name":"dineshbro","no":893921595,"emailid":"diunesh@gmail.com","groups":"friends"},
                                {"name":"divya aka","no":6380848540,"emailid":"divya@gmail.com","groups":"family"},{"name":"divya school","no":8428230524,"emailid":"divyaa@gmail.com","groups":"friends"},
                                {"name":"gajalakshmi","no":9790732962,"emailid":"gajalak@gmail.com","groups":"family"},{"name":"gayu","no":9962482108,"emailid":"gayuuu@gmail.com","groups":"family"},
                                {"name":"gayu2","no":996248210,"emailid":"gayui@gmail.com","groups":"friends"},{"name":"gopika","no":7338802855,"emailid":"gopika@gmail.com","groups":"friends"},
                                {"name":"haritha","no":6379471217,"emailid":"haru@disys.com","groups":"friends"},{"name":"hema","no":7401145743,"emailid":"hema@gmail.com","groups":"family"},
                                {"name":"honeybee","no":7010476992,"emailid":"honeybee@disys.com","groups":"friends"},{"name":"indhu","no":6382621170,"emailid":"indhumarhi@disys.com","groups":"family"},
                                {"name":"ishwarya","no":9840501867,"emailid":"ish@gmail.com","groups":"colleagues"},{"name":"janani","no":9790823780,"emailid":"janani@disys.com","groups":"colleagues"},
                                {"name":"jananiya","no":8925177357,"emailid":"jananiya@gmail.com","groups":"friends"},{"name":"jegadeesh","no":8111089445,"emailid":"jegadeesh@gmail.com","groups":"friends"},
                                {"name":"jeyadev","no":8667639927,"emailid":"jeyadev@gmail.com","groups":"colleagues"},{"name":"judysimon","no":8925438717,"emailid":"judy@gmail.com","groups":"family"},
                                {"name":"juni","no":6374508861,"emailid":"juni@gmail.com","groups":"colleagues"},{"name":"kani","no":7397468780,"emailid":"kani@gmail.com","groups":"family"},
                                {"name":"kavya","no":9941027762,"emailid":"kavya@gmail.com","groups":"friends"},{"name":"maha","no":9092042867,"emailid":"maha@disys.com","groups":"friends"},
                                {"name":"manoj","no":6303388297,"emailid":"manoj@disys.com","groups":"colleagues"},{"name":"mohanapriya","no":9790897459,"emailid":"mohana@gmail.com","groups":"friends"},
                                {"name":"narayanan","no":6382528639,"emailid":"nara@gmail.com","groups":"family"},{"name":"oviya","no":7259964362,"emailid":"ovi@gmail.com","groups":"friends"}]          

for i in phonenumberlist:
    for j,k in i.items():
        print( f"{j}:{k}")


                                                                                                                   
                                                                                                                   
                                                                                                                   
                                                                                                                   
