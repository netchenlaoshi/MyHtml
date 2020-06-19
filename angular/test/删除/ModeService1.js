var model=angular.module('nameList.model',[]);


function Guest(name,phone){
    this.name=name;
    this.phone=phone;
    this.state = Guest.INVITE;
}

Guest.INVITE = '邀请中';
Guest.ACCEPT = '已接受';
Guest.REFUSE = '已拒绝';

Guest.prototype.accept = function () {
    this.state = Guest.ACCEPT;
}

Guest.prototype.refuse = function () {
    this.state = Guest.REFUSE;
}

model.factory('modelService',function(){
    var guestList={
        list:[],
        add:function(name,phone){
            var guest=new Guest(name,phone);
            this.list.push(guest);
        },

        remove: function (guest) {
            this.list = this.list.filter(function (item) {
                return guest.phone != item.phone;
            })
        },
        
        getList:function(state){
            if(state ==Guest.ALL){
                return this.list.filter(function(){
                    return true;
                })
            }
        }
    }
    return guestList;
})