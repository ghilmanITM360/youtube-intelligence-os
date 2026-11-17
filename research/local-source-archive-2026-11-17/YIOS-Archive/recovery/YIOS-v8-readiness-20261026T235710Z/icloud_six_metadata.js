ObjC.import('Foundation');
var input=$.NSString.stringWithContentsOfFileEncodingError('/Users/ghilmankhan/YIOS-v8-readiness-20261026T235710Z/evidence/ICLOUD_SIX_PATHS.json',$.NSUTF8StringEncoding,null);
var paths=JSON.parse(ObjC.unwrap(input));
var keys=['NSURLIsUbiquitousItemKey','NSURLUbiquitousItemDownloadingStatusKey','NSURLUbiquitousItemIsUploadedKey','NSURLUbiquitousItemIsUploadingKey','NSURLUbiquitousItemIsDownloadingKey','NSURLUbiquitousItemHasUnresolvedConflictsKey','NSURLUbiquitousItemUploadingErrorKey','NSURLUbiquitousItemDownloadingErrorKey'];
var out=[];paths.forEach(function(p){var u=$.NSURL.fileURLWithPath(p);var err=Ref();var vals=u.resourceValuesForKeysError($(keys),err);out.push({path:p,values:vals?ObjC.deepUnwrap(vals):null,error:err[0]?ObjC.unwrap(err[0].localizedDescription):null});});
JSON.stringify(out,null,2);
