'use strict';
/**
 * Created by berluskuni on 26.09.16.
 */
var module = angular.module('alexApp', ['ui.router','ui.bootstrap']);
module.config(function($interpolateProvider){
    $interpolateProvider.startSymbol('[[').endSymbol(']]')
});
module.config(function($stateProvider, $locationProvider){
    $locationProvider.html5Mode({
        enabled: true,
        requireBase: false
    });
    var homeState = {
        name: 'home',
        url: '/',
        templateUrl: '/static/template/home.html'
    };
    $stateProvider.state(homeState);
});
