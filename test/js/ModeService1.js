var model=angular.module('nameList.model',[]);


function Guest(name,phone){
    this.name=name;
    this.phone=phone;
    this.state = Guest.INVITE;
}

Guest.INVITE = '邀请中';
Guest.ACCEPT = '已接受';

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

        
        getList:function(state){
            if (state==Guest.ALL){
                return this.list.filter(function(){
                    return true;
                })
            }
            return this.list.filter(function (guest){
                return guest.state==state;
            })
        }
    }
    return guestList;
})