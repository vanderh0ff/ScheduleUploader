import lxml
import requests
import calendar

class Schedule:
    """Schedule takes in a file location for a settings file 
    that contains the following
    the path to the text file copied from banner
    the url of the school callendar
    the path to export the csv to
    """

    def __init__(self):
        self.session = requests.session()

    @classmethod
    def get_school_calendar(cls):
        """TODO: Docstring for get_school_calendar.
        :returns: TODO
        """
        pass


    @classmethod
    def parse_banner(cls, banner_path):
        """ takes the banner output and puts it in google compatible csv form
        :banner_path: TODO
        :returns: TODO
        """
        outcsv = open(r'C:\Users\matt\Desktop\calendar.csv','w')
        outcsv.write("Subject,Start Date,End Date,Start Time,End Time,Location\n")
        cal = calendar.Calendar()
        samplesched = "20427	COMM 2105-004 	Small Group Communication	3	01/11 - 05/03	MW 	 12:30p-1:45p 	DENNY 105 	Baker, Debra \n\
24224	ITIS 2211-266 	Eth Iss Per Prof Pub Life:Tech	3	01/11 - 05/03	WF 	 9:30a-10:45a 	FRIDY 142 	Riley, Sean\n\
24636	MATH 2164-007 	Matrices & Linear Algebra	3	01/11 - 05/03	TTh 	 3:30p-4:45p 	COLVD 3066 	Sonin, Isaac\n\
27332	HIST 3000-A90 	Topics in US History	3	01/11 - 05/03	TTh 	 5:00p-6:15p 	FRIDY 381 	Klehr, Gabriel \n\
27940	ITCS 3688-006 	Comp & Their Impact on Society	3	01/11 - 05/03	Th 	 9:30a-12:15p 	CHHS 159 	Wilson, Dale-Marie"
        sched = []
        for line in samplesched.split('\n'):
            fields = line.split('\t')
            subject = fields[2]
            dates = fields[4].split('-')
            startdate = dates[0]
            startmonth = startdate.split('/')[0]
            startday = startdate.split('/')[1]
            enddate = dates[1]
            endmonth = enddate.split('/')[0]
            endday = enddate.split('/')[1]
            days = fields[5]
            times = fields[6].split('-')
            starttime = times[0].strip()
            endtime = times[1].strip()
            location = fields[7]
            numdays = []
            if  days.strip() == "MW":
                numdays = [0,2]
            elif  days.strip() == "TTh":
                numdays = [1,3]
            elif  days.strip() == "Th":
                numdays = [3]
            elif  days.strip() == "WF":
                numdays = [2,4]
            for x in range(int(startmonth.strip()),int(endmonth.strip())):
                monthcal = cal.monthdatescalendar(2016,x)
                for w in monthcal:
                    for d in numdays:
                        outcsv.write("{},{},{},{},{},{}".format(subject,str(w[d]).replace('-','/'),str(w[d]).replace('-','/'),starttime[:-1]+" {}m".format(starttime[-1]),endtime[:-1]+" {}m".format(endtime[-1]),location+'\n'))


                
mysch = Schedule()
mysch.parse_banner('no path')

