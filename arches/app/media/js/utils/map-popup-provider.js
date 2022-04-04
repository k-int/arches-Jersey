define(['arches',
    'knockout',
    'text!templates/views/components/map-popup.htm'
], function (arches, ko, popupTemplate) {

    var provider = {

        /**
         * Callback to determine if the feature is clickable
         * @param feature Map feature to check
         * @returns <code>true</code> if the feature can be clicked, otherwise <code>false</code>
         */
        isFeatureClickable: function (feature) {
            return feature.properties.resourceinstanceid;
        },

        /**
         * Return the template that should be used for the
         * @param features
         * @returns {*}
         */
        getPopupTemplate: function(features)
        {
            return popupTemplate;
        },

        /**
         * Each feature in the list must have a <code>displayname</code> and <code>map_popup</code> value. This is
         * handled for arches resources by the framework, but can be injected here if any of the features.popupFeatures
         * do not have one.
         */
        processData: function(features)
        {
            return features;
        },

    };
    return provider;
});
