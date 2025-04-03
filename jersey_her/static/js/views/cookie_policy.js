require([
    'views/base-manager',
    'bindings/datatable'
], function(BaseManagerView) {
    /**
    * a BaseManagerView representing the recent edits pages
    */
    var CookiePolicy = BaseManagerView.extend({
        initialize: function(options){
            
            BaseManagerView.prototype.initialize.call(this, options);
        }
    });
    return new CookiePolicy();
});
