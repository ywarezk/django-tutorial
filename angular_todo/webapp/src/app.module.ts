/**
 * root module
 */

import 'reflect-metadata';
import 'zone.js';
import {NgModule} from '@angular/core';
import {AppComponent} from "./components/app.component";
import {platformBrowserDynamic} from '@angular/platform-browser-dynamic';
import {BrowserModule} from '@angular/platform-browser';

@NgModule({
    declarations: [AppComponent],
    bootstrap: [AppComponent],
    imports: [BrowserModule]
})
export class AppModule{

}

platformBrowserDynamic().bootstrapModule(AppModule);