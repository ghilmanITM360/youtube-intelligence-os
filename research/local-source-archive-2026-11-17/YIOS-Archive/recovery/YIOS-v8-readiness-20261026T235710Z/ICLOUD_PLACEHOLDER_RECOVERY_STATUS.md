# iCloud status — bounded evidence, not whole-account certification

Roman Urdu: Pichle audit ke7,359 placeholders ko lost nahi kaha ja sakta. Apple metadata ke8chhote samples uploaded/not-downloaded the aur sab ke poore13,656bytes read hue. Saved gap list ke6script archive copies ke77,142bytes bhi hydrate hue aur canonical hashes se match hain. Total14paths/90,798bytes. Baqi7,345previously listed paths is task mein read nahi hue; unki current condition unknown hai. Yeh arithmetic hai, naya global placeholder census nahi.

The six archive copies were encountered during selected saved-path gap hashing, not an indiscriminate scan. Their initial pass observed timestamp changes; a stable resident reread matched all six exact canonical hashes. Foundation metadata afterwards reports Current, uploaded=true, uploading=false, no unresolved conflicts. We do not call this an immutable/version-retained backup or prove account-wide synchronization.

Eight original sample metadata queries reported uploaded=true, uploading=false, downloading=false, NotDownloaded, no unresolved conflicts. Read success confirms bounded provider accessibility. The first six nonempty sample files total13,656bytes; two zero-byte historical files remain zero-byte artifacts, not proof of substantive contents. Historic version hashes for those samples remain unknown except independently matched equivalences listed in evidence/ICLOUD_READ_SAMPLE_RECONCILED.json.

Hydration changed dataless/download flags and sub-microsecond mtime values. The audit wrote no source content; it cannot claim every source metadata field remained unchanged. No optimization setting, move, sign-out, permission or bulk request was performed. Private retained scratch is within this audit output. Download accounting conservatively includes all90,798bytes.

Apple-supported interpretation: [Finder iCloud status](https://support.apple.com/en-gb/guide/mac-help/mchlc994344b/27/mac/27) distinguishes Waiting to Upload from downloaded/cloud-only items. [Foundation download status](https://developer.apple.com/documentation/foundation/urlubiquitousitemdownloadingstatus) supplies metadata, which is not a content hash.

Owner checklist: inspect Finder iCloud Status for the four approved Documents roots, confirm intended Apple account without disclosing credentials, note Waiting to Upload/Out of Space/conflicts, select a few important originals with historical hashes for a separately bounded test. Obtain exact historical hashes and retained version/export policy. Do not hydrate folders, disable optimization, sign out, move originals or infer all remaining files synced. No account-wide pending-upload count or full version retention evidence was available through the bounded file metadata reads.

Evidence: evidence/ICLOUD_METADATA_SAMPLE.json; ICLOUD_READ_SAMPLE_RECONCILED.json; ICLOUD_SIX_SCRIPT_COPIES.json; ICLOUD_SIX_METADATA.json. No Apple account credential data captured.
