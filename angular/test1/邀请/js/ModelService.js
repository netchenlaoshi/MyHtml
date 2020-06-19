var model=angular.module('nameList.model',[]);

function Guest(name,phone){
    this.name=name;
    this.phone=phone;
}

model.factory('modelService',function(){
    var guestList = {
        list: [],
        add: function (name, phone) {
            var guest = new Guest(name, phone);
            this.list.push(guest);
            },
        getList:function(){
            return this.list.filter(function(){
                return true;
            })
        }
    } 
    return guestList;   
})
