/*
 * Copyright 2016, GeoSolutions Sas.
 * All rights reserved.
 *
 * This source code is licensed under the BSD-style license found in the
 * LICENSE file in the root directory of this source tree.
 */
const React = require('react');
const {connect} = require('react-redux');

const {toggleControl} = require('../../MapStore2/web/client/actions/controls');
const {updateNaturalFeature, deleteNaturalFeature} = require('../actions/naturalfeatures');
const {changeDrawingStatus, endDrawing} = require('../../MapStore2/web/client/actions/draw');

const DockedNaturalFeatures = require('../components/naturalfeatures/DockedNaturalFeatures');
const SmartDockedNaturalFeatures = connect((state) => ({
    isVisible: state.controls.vieweditnaturalfeatures && state.controls.vieweditnaturalfeatures.enabled,
    naturalFeatureType: state.naturalfeatures.naturalFeatureType,
    currentFeature: state.naturalfeatures.selectedFeature,
    dockSize: state.naturalfeatures.dockSize,
    mode: state.naturalfeatures.mode,
    isAdmin: true
}), {
    onToggle: toggleControl.bind(null, 'vieweditnaturalfeatures', null),
    onUpdate: updateNaturalFeature.bind(null),
    onDelete: deleteNaturalFeature.bind(null),
    onChangeDrawingStatus: changeDrawingStatus,
    onEndDrawing: endDrawing
})(DockedNaturalFeatures);

const ViewEditNaturalFeaturesPlugin = React.createClass({
    render() {
        return (
            <div>
                <SmartDockedNaturalFeatures mode="viewedit"/>
            </div>
        );
    }
});

module.exports = {
    ViewEditNaturalFeaturesPlugin,
    reducers: {
        naturalfeatures: require('../reducers/naturalfeatures')
    }
};
