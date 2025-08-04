define([
    'knockout',
    'templates/views/components/widgets/geometry-type.htm',
], function(ko, geometryTypeTemplate) {
    const geometryTypeViewModel = function (params) {
        let self = this;

        this.count = params.count;
        this.label = params.label;
        this.expanded = params.expanded;
        this.bulletPoints = params.bulletPoints;

        this.toggleExpanded = function () {
            self.expanded(!self.expanded());
        };
    };

    return ko.components.register('geometry-type', {
        viewModel: geometryTypeViewModel,
        template: geometryTypeTemplate,
    });
});