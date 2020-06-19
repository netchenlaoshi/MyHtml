var model = angular.module('nameList.model', []);
function Guest(name, phone) {
    this.name = name;
    this.phone = phone;
    this.state = Guest.INVITE;
}


    model.factory('modelService', function () {
        var guestList = {
            list: [],
            add: function (name, phone) {
                var guest = new Guest(name, phone);
                this.list.push(guest)
                
            
            },

            getList:function(state){
                
                if (state==Guest.ALL){
                        return this.list.filter(function(){
                            return true;
                        })
                    }
                    return this.list.filter(function (guest){
                        return guest.state==state;
                    })
                        
                    },
                        
                        
            remove: function (guest) {
                        this.list = this.list.filter(function (item) {
                            return guest.phone != item.phone;
                        })
                    },
                
            }
            return guestList;
        
            
    });
    
   
    Guest.INVITE = '邀请中';
    Guest.ALL = '全部';
    Guest.ACCEPT = '已接受';
    Guest.prototype.accept = function () {
        this.state = Guest.ACCEPT;
    }

