/* tslint:disable */
/* eslint-disable */
/**
 * 簡易物品管理WebAPI
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { exists, mapValues } from '../runtime';
/**
 * 痕跡
 * @export
 * @interface Footprint
 */
export interface Footprint {
    /**
     * 作成日時
     * @type {Date}
     * @memberof Footprint
     */
    createdAt?: Date;
    /**
     * 作成者ID
     * @type {string}
     * @memberof Footprint
     */
    createdBy?: string;
    /**
     * 更新日時
     * @type {Date}
     * @memberof Footprint
     */
    updatedAt?: Date;
    /**
     * 更新者ID
     * @type {string}
     * @memberof Footprint
     */
    updatedBy?: string;
}

export function FootprintFromJSON(json: any): Footprint {
    return FootprintFromJSONTyped(json, false);
}

export function FootprintFromJSONTyped(json: any, ignoreDiscriminator: boolean): Footprint {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'createdAt': !exists(json, 'createdAt') ? undefined : (new Date(json['createdAt'])),
        'createdBy': !exists(json, 'createdBy') ? undefined : json['createdBy'],
        'updatedAt': !exists(json, 'updatedAt') ? undefined : (new Date(json['updatedAt'])),
        'updatedBy': !exists(json, 'updatedBy') ? undefined : json['updatedBy'],
    };
}

export function FootprintToJSON(value?: Footprint | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'createdAt': value.createdAt === undefined ? undefined : (value.createdAt.toISOString()),
        'createdBy': value.createdBy,
        'updatedAt': value.updatedAt === undefined ? undefined : (value.updatedAt.toISOString()),
        'updatedBy': value.updatedBy,
    };
}

