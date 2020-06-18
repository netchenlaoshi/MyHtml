var model = angular.module('nameList.model', []);
function Guest(name, phone) {
    this.name = name;
    this.phone = phone;
}


    model.factory('modelService', function () {
        var guestList = {
            list: [],
            add: function (name, phone) {
            var guest = new Guest(name, phone);
                this.list.push(guest)
            },

            getList:function(state){
                    
                        return this.list.filter(function(){
                            return true;
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
    
    Guest.REFUSE = '已拒绝';
    Guest.prototype.refuse = function () {
        this.state = Guest.REFUSE;
        
            }
