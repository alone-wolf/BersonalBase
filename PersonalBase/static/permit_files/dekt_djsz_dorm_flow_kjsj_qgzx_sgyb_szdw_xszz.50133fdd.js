(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["dekt~djsz~dorm~flow~kjsj~qgzx~sgyb~szdw~xszz"],{"2b03":function(t,e,a){"use strict";var r=a("4ea4");Object.defineProperty(e,"__esModule",{value:!0}),e.default=void 0;var o=r(a("4db1"));a("96cf");var n=r(a("fa84"));a("ac4d"),a("8a81"),a("ac6a"),a("c5f6");var l=r(a("53fe")),i=a("4ec3"),s={name:"ExportExcel",props:{dcclbh:{required:!0},dataUrl:{type:String,required:!0},dataParams:{type:Object,default:function(){return{}}},totalCount:{type:Number,default:1e5},excelName:{type:String,default:""},hasPagination:{type:Boolean,default:!0}},data:function(){return{dialogVisible:!1,exportThData:[],exportThValue:[],dcclmc:"",phList:[],excelData:[],loading:""}},methods:{handleClose:function(){this.step=1,this.dialogVisible=!1},openExportDialog:function(){this.$isEmpty(this.dcclbh)?this.$message.error("请配置导出代码！"):this.totalCount<1?this.$message.error("导出列表为空！"):(this.getConfigList(),this.dialogVisible=!0,this.$nextTick(function(){this.dragSort()}))},getConfigList:function(){var t=this;this.phList=[],this.exportThData=[],(0,i.apiExportConfig)({dcclbh:this.dcclbh}).then(function(e){if(0==e.code){t.phList=e.data.phList;var a=e.data.configList;if(t.$isNotEmpty(a)){t.dcclmc=a[0].dcclmc;var r=!0,o=!1,n=void 0;try{for(var l,i=a[Symbol.iterator]();!(r=(l=i.next()).done);r=!0){var s=l.value;t.exportThData.push({key:s.zd,label:s.zdmc})}}catch(c){o=!0,n=c}finally{try{r||null==i.return||i.return()}finally{if(o)throw n}}}}})},saveSettings:function(){var t=this;this.$prompt("请输入快照名称","快照名称",{confirmButtonText:"确定",cancelButtonText:"取消",inputPattern:/\S/,inputErrorMessage:"快照名称不能为空！"}).then(function(e){var a=e.value,r=[],o=!0,n=!1,l=void 0;try{for(var s,c=t.exportThValue[Symbol.iterator]();!(o=(s=c.next()).done);o=!0){var d=s.value,u=!0,p=!1,f=void 0;try{for(var h,m=t.exportThData[Symbol.iterator]();!(u=(h=m.next()).done);u=!0){var v=h.value;v.key===d&&r.push(v.key+"!_##_!"+v.label)}}catch(g){p=!0,f=g}finally{try{u||null==m.return||m.return()}finally{if(p)throw f}}}}catch(g){n=!0,l=g}finally{try{o||null==c.return||c.return()}finally{if(n)throw l}}var b={dcclbh:t.dcclbh,exportPHMC:a,selecZd:r.join(",")};(0,i.apiSaveCustomConfig)(b).then(function(e){0===e.code&&t.phList.push({id:e.data.exportPHID,mc:e.data.exportPHMC})})}).catch(function(){})},delPh:function(t){var e=this,a={exportPHID:t.id};(0,i.apiDeleteCustomConfig)(a).then(function(a){0===a.code&&e.phList.remove(t)})},selectPh:function(t){var e=this;(0,i.apiCxConfigPhZdList)({exportPHID:t.id}).then(function(t){if(0===t.code){e.exportThValue=[];var a=!0,r=!1,o=void 0;try{for(var n,l=t.data[Symbol.iterator]();!(a=(n=l.next()).done);a=!0){var i=n.value;e.exportThValue.push(i.zd);var s=!0,c=!1,d=void 0;try{for(var u,p=e.exportThData[Symbol.iterator]();!(s=(u=p.next()).done);s=!0){var f=u.value;f.key===i.zd&&(e.exportThData.remove(f),e.exportThData.push(f))}}catch(h){c=!0,d=h}finally{try{s||null==p.return||p.return()}finally{if(c)throw d}}}}catch(h){r=!0,o=h}finally{try{a||null==l.return||l.return()}finally{if(r)throw o}}}})},dragSort:function(){var t=this,e=document.querySelectorAll(".export-dialog .el-checkbox-group")[1];this.sortable=l.default.create(e,{onEnd:function(e){var a=t.exportThValue.splice(e.oldIndex,1)[0];t.exportThValue.splice(e.newIndex,0,a)}})},exportExe:function(){var t=(0,n.default)(regeneratorRuntime.mark(function t(){var e=this;return regeneratorRuntime.wrap(function(t){while(1)switch(t.prev=t.next){case 0:if(""!=this.exportThValue){t.next=4;break}this.$message.warning("已选导出列为空！"),t.next=5;break;case 4:return t.delegateYield(regeneratorRuntime.mark(function t(){var a,r,n,l,s;return regeneratorRuntime.wrap(function(t){while(1)switch(t.prev=t.next){case 0:e.loading=e.$loading({lock:!0,text:"正在导出...",spinner:"el-icon-loading",background:"rgba(0, 0, 0, 0.7)"}),a=JSON.parse(JSON.stringify(e.dataParams)),r=4e4,n=Math.ceil(e.totalCount/r),l=[],s=0;case 5:if(!(s<n)){t.next=18;break}return e.hasPagination&&Object.assign(a,{showCount:r,currentPage:s+1}),t.prev=7,t.next=10,(0,i.apiPost)(e.dataUrl,a,"urlencoded").then(function(t){0===t.code&&(l=e.$isEmpty(t.queryModel)?[].concat((0,o.default)(l),(0,o.default)(t.data.rows||t.data.items||t.data)):[].concat((0,o.default)(l),(0,o.default)(t.queryModel.items)))});case 10:t.next=15;break;case 12:t.prev=12,t.t0=t["catch"](7),console.log("e:",t.t0);case 15:s++,t.next=5;break;case 18:e.export2Excel(l);case 19:case"end":return t.stop()}},t,null,[[7,12]])})(),"t0",5);case 5:case"end":return t.stop()}},t,this)}));function e(){return t.apply(this,arguments)}return e}(),export2Excel:function(t){var e=this,r=[],o=!0,n=!1,l=void 0;try{for(var i,s=this.exportThValue[Symbol.iterator]();!(o=(i=s.next()).done);o=!0){var c=i.value,d=!0,u=!1,p=void 0;try{for(var f,h=this.exportThData[Symbol.iterator]();!(d=(f=h.next()).done);d=!0){var m=f.value;m.key===c&&r.push(m.label)}}catch(v){u=!0,p=v}finally{try{d||null==h.return||h.return()}finally{if(u)throw p}}}}catch(v){n=!0,l=v}finally{try{o||null==s.return||s.return()}finally{if(n)throw l}}a.e("chunk-4d429307").then(function(){var o=a("51ce"),n=o.export_json_to_excel,l=e.formatJson(e.exportThValue,t);n(r,l,"".concat(e.dcclmc||e.excelName))}.bind(null,a)).catch(a.oe),this.loading.close(),this.dialogVisible=!1},formatJson:function(t,e){return e.map(function(e){return t.map(function(t){return e[t]})})}}};e.default=s},5725:function(t,e,a){"use strict";var r=a("4ea4");Object.defineProperty(e,"__esModule",{value:!0}),e.default=void 0,a("5df3"),a("4f7f");var o=r(a("4db1"));a("ac4d"),a("8a81"),a("ac6a");var n=a("4ec3"),l={name:"ImportExcel",props:{drmkdm:{required:!0}},data:function(){return{step:1,dialogVisible:!1,importConfig:[],importRules:[],fileList:[],hasUploadExcel:!1,importWays:[],importWay:"1",checkAll:!1,isIndeterminate:!0,trueColumns:[],requiredColumns:[],checkedColumns:[],importColumns:[],hasZj:!1,hasError:!1}},methods:{openImportDialog:function(){var t=this;this.$nextTick(function(){t.$isEmpty(t.drmkdm)?t.$message.error("请配置导入代码！"):t.getImportConfig()})},getImportConfig:function(){var t=this;(0,n.apiGetImportConfig)({drmkdm:this.drmkdm}).then(function(e){0===e.code?(t.importConfig=e.data,t.getRulers(),t.dialogVisible=!0):console.log("drmkdm:",t.drmkdm)})},getRulers:function(){var t=this;(0,n.apiGetRulers)({drmkdm:this.drmkdm}).then(function(e){0===e.code&&(t.importRules=e.data)})},uploadOnSuccess:function(t){0==t.code?this.getImportRow():this.$message.warning(t.msg)},getImportRow:function(){var t=this;(0,n.apiGetImportColumn)({drmkdm:this.drmkdm}).then(function(e){if(0===e.code){t.hasUploadExcel=!0,t.importWays=e.data.crfs,t.importWay=t.importWays[0].id,t.importColumns=e.data.columns,t.hasError=!1;var a=!0,r=!1,o=void 0;try{for(var n,l=t.importColumns[Symbol.iterator]();!(a=(n=l.next()).done);a=!0){var i=n.value;2==i.valid?(1==i.sfzj&&(t.hasZj=!0),t.trueColumns.push(i.drlpzid),t.checkedColumns.push(i.drlpzid),1!=i.sfzj&&1!=i.sfbt||t.requiredColumns.push(i.drlpzid)):0==i.valid&&(t.hasError=!0)}}catch(s){r=!0,o=s}finally{try{a||null==l.return||l.return()}finally{if(r)throw o}}t.handleCheckedColumnsChange(t.checkedColumns)}})},importExe:function(){var t=this,e={drlpzids:this.checkedColumns.join(","),drmkdm:this.drmkdm,crfs:this.importWay};(0,n.apiImportData)(e).then(function(e){if(0===e.code){t.handleClose();var a=e.data;"v1"===a.version&&(a.result>0?a.totalSize>0?t.$alert('<strong>全部成功</strong><p class="tip">共执行'.concat(a.totalSize,"条，其中插入").concat(a.successInsertRowsSize,"条，更新").concat(a.successUpdateRowsSize,"条</p>"),"导入",{dangerouslyUseHTMLString:!0,customClass:"alert-dialog",type:"success",callback:function(){t.$emit("refreshData")}}):t.$message.warning("导入文件数据为空，请添加后再导入！"):"0"==a.result?t.$alert('<strong>部分失败</strong>\n<p class="tip">共执行'.concat(a.totalSize,"条，其中插入").concat(a.successInsertRowsSize,"条，错误<b>").concat(a.totalUnAcceptRowSize,'</b>条</p>\n<p class="tip"><i class="el-icon-info"></i>点击错误内容\n<a class="link" href=\'').concat(t.GLOBAL.BASE_URL,"/xgdrdc/import/downloadError.zf?drmkdm=").concat(t.drmkdm,"&resultFileId=").concat(a.resultFileId,"'>下载></a></p>"),"导入",{dangerouslyUseHTMLString:!0,customClass:"alert-dialog",type:"error"}):"-1"===a.result&&t.$message.error("系统内部错误"))}})},handleCheckAllChange:function(t){this.checkedColumns=t?(0,o.default)(new Set([].concat((0,o.default)(this.trueColumns),(0,o.default)(this.requiredColumns)))):this.requiredColumns,this.isIndeterminate=!1},handleCheckedColumnsChange:function(t){var e=t.length;this.checkAll=e===this.trueColumns.length,this.isIndeterminate=e>0&&e<this.trueColumns.length},handleClose:function(){this.dialogVisible=!1,this.step=1,this.fileList=[],this.hasUploadExcel=!1}}};e.default=l},"5f1d":function(t,e,a){"use strict";a.r(e);var r=a("6df7"),o=a("95ac");for(var n in o)"default"!==n&&function(t){a.d(e,t,function(){return o[t]})}(n);var l=a("2877"),i=Object(l["a"])(o["default"],r["a"],r["b"],!1,null,null,null);e["default"]=i.exports},"6df7":function(t,e,a){"use strict";var r=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("el-dialog",{staticClass:"export-dialog",attrs:{title:"导出",visible:t.dialogVisible,width:"550px","before-close":t.handleClose,"close-on-click-modal":!1,"lock-scroll":!0,"append-to-body":"","modal-append-to-body":""},on:{"update:visible":function(e){t.dialogVisible=e}}},[a("el-transfer",{attrs:{titles:["可选导出列","已选导出列"],data:t.exportThData},model:{value:t.exportThValue,callback:function(e){t.exportThValue=e},expression:"exportThValue"}}),a("hr",{staticClass:"dashed"}),""!=t.phList?a("div",{staticClass:"export-snapshot"},[t._v("\n    导出快照："),t._l(t.phList,function(e){return a("el-tag",{key:e.id,attrs:{closable:"",size:"small"},on:{close:function(a){return t.delPh(e)}},nativeOn:{click:function(a){return t.selectPh(e)}}},[t._v("\n      "+t._s(e.mc)+"\n    ")])})],2):a("div",{staticClass:"export-snapshot"},[t._v("导出快照："),a("b",[t._v("无")])]),a("div",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[a("el-button",{on:{click:t.saveSettings}},[t._v("保存设置")]),a("el-button",{attrs:{type:"primary"},on:{click:t.exportExe}},[t._v("导出EXCEL")])],1)],1)},o=[];a.d(e,"a",function(){return r}),a.d(e,"b",function(){return o})},"95ac":function(t,e,a){"use strict";a.r(e);var r=a("2b03"),o=a.n(r);for(var n in r)"default"!==n&&function(t){a.d(e,t,function(){return r[t]})}(n);e["default"]=o.a},b711:function(t,e,a){"use strict";a.r(e);var r=a("de45"),o=a("ec9f");for(var n in o)"default"!==n&&function(t){a.d(e,t,function(){return o[t]})}(n);var l=a("2877"),i=Object(l["a"])(o["default"],r["a"],r["b"],!1,null,null,null);e["default"]=i.exports},de45:function(t,e,a){"use strict";var r=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("el-dialog",{staticClass:"import-dialog",attrs:{title:"导入",visible:t.dialogVisible,width:"800px","before-close":t.handleClose,"close-on-click-modal":!1,"lock-scroll":!0,"append-to-body":"","modal-append-to-body":""},on:{"update:visible":function(e){t.dialogVisible=e}}},[a("div",{directives:[{name:"show",rawName:"v-show",value:1==t.step,expression:"step == 1"}],staticClass:"step-1"},[a("h4",[a("i",{staticClass:"el-icon-download"}),t._v(" 导入数据")]),a("el-form",{attrs:{"label-position":"right","label-width":"120px"}},[a("el-form-item",{attrs:{label:"模板名称:"}},t._l(t.importConfig,function(e){return a("span",{key:e.drmkdm},[t._v(t._s(e.drmkmc)+" "),a("a",{staticClass:"link",attrs:{href:t.GLOBAL.BASE_URL+"/xgdrdc/import/downloadTemplate.zf?drmkdm="+e.drmkdm,download:e.drmkmc+"导入模板"}},[t._v("EXCEL模板下载")])])}),0),a("el-form-item",{attrs:{label:"上传文件:",rules:[{required:!0,message:"请上传文件"}]}},[a("el-upload",{attrs:{action:t.GLOBAL.BASE_URL+"/xgdrdc/import/uploadExcel.zf",limit:1,"file-list":t.fileList,name:"importFile","on-success":t.uploadOnSuccess}},[a("el-button",{attrs:{size:"small",type:"primary"}},[t._v("点击上传")]),a("div",{staticClass:"el-upload__tip",attrs:{slot:"tip"},slot:"tip"},[t._v("只能支持xls/xlsx文件")])],1)],1)],1),a("hr",{staticClass:"dashed"}),a("h4",[a("i",{staticClass:"el-icon-warning"}),t._v(" 导入规则")]),a("el-table",{attrs:{data:t.importRules,border:""}},[a("el-table-column",{attrs:{prop:"drlmc",label:"列名称"}}),a("el-table-column",{attrs:{prop:"sfzj",label:"是否主键"},scopedSlots:t._u([{key:"default",fn:function(e){return["1"===e.row.sfzj?a("i",{staticClass:"el-icon-check"}):t._e()]}}])}),a("el-table-column",{attrs:{prop:"sfwy",label:"是否唯一"},scopedSlots:t._u([{key:"default",fn:function(e){return["1"===e.row.sfwy?a("i",{staticClass:"el-icon-check"}):t._e()]}}])}),a("el-table-column",{attrs:{prop:"sfbt",label:"不可为空"},scopedSlots:t._u([{key:"default",fn:function(e){return["1"===e.row.sfbt?a("i",{staticClass:"el-icon-check"}):t._e()]}}])}),a("el-table-column",{attrs:{prop:"zdcd",label:"最大长度"}}),a("el-table-column",{attrs:{prop:"gshxx",width:"200",label:"数据格式"}})],1)],1),2==t.step?a("div",{staticClass:"step-2"},[a("el-form",{attrs:{"label-position":"right","label-width":"100px"}},[a("el-form-item",{attrs:{label:"导入方式:"}},t._l(t.importWays,function(e){return a("el-radio",{key:e.id,attrs:{label:e.id},model:{value:t.importWay,callback:function(e){t.importWay=e},expression:"importWay"}},[t._v(t._s(e.name))])}),1),a("el-form-item",{staticClass:"import-columns",attrs:{label:"导入列:"}},[a("el-checkbox",{attrs:{indeterminate:t.isIndeterminate},on:{change:t.handleCheckAllChange},model:{value:t.checkAll,callback:function(e){t.checkAll=e},expression:"checkAll"}},[t._v("全选 ")]),a("el-checkbox-group",{staticClass:"checkbox-group",on:{change:t.handleCheckedColumnsChange},model:{value:t.checkedColumns,callback:function(e){t.checkedColumns=e},expression:"checkedColumns"}},t._l(t.importColumns,function(e){return a("el-checkbox",{key:e.drlpzid,class:"color-"+e.valid,attrs:{disabled:1==e.locked,label:e.drlpzid,title:e.title}},[t._v("\n            "+t._s(e.drlmc)+"\n          ")])}),1)],1)],1),a("div",{staticClass:"instructions"},[a("div",{staticClass:"title"},[a("i",{staticClass:"el-icon-warning"}),a("span",[t._v("帮助提示")])]),a("div",{staticClass:"content"},[a("p",[t._v("1. 导入方式为 ‘插入’ 或 ‘插入并更新’ 时，必填项默认全部选中，且选中状态不可取消，不必填项可选择插入或更新。")]),a("p",[t._v("2. 导入方式为 ‘更新’ 时，主键项默认选中，且选中状态不可取消, 其他项可选择更新。")]),a("p",[t._v("3. 当导入数据中存在其他错误数据列时，系统将提示 ‘没有对应列，此列不导入’， 并且该列不能导入。")]),a("p",[t._v("4. 当导入时，缺少必要的必填项列时，系统将提示 ‘必填列，列必须存在导入模板中’ 。")])])])],1):t._e(),a("div",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[1==t.step?a("el-button",{on:{click:t.handleClose}},[t._v("取 消")]):t._e(),1==t.step?a("el-button",{attrs:{type:"primary",disabled:!t.hasUploadExcel},on:{click:function(e){t.step=2}}},[t._v("下一步")]):t._e(),2==t.step?a("el-button",{attrs:{type:"primary"},on:{click:function(e){t.step=1}}},[t._v("上一步")]):t._e(),2==t.step?a("el-button",{attrs:{type:"primary",disabled:t.hasError},on:{click:t.importExe}},[t._v("确定")]):t._e()],1)])},o=[];a.d(e,"a",function(){return r}),a.d(e,"b",function(){return o})},ec9f:function(t,e,a){"use strict";a.r(e);var r=a("5725"),o=a.n(r);for(var n in r)"default"!==n&&function(t){a.d(e,t,function(){return r[t]})}(n);e["default"]=o.a}}]);