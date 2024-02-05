import { AxiosResponse } from 'axios';
import request from '@/api/request'
import base from '@/api/base';

/* 
 * 登录
 * data: { Username, Password }
 */
export function LoginApi(params: object): Promise<AxiosResponse> {
  return request({
    url: base.login,
    method: 'post',
    data: params,
  })
}
