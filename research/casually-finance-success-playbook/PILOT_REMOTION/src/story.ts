export const FPS = 30;
export const DURATION = 1260;
export const lines = [
 {id:'hook', text:'The Fed cuts rates. Your mortgage payment? Still the same.', caption:'Rates down. Payment unchanged.'},
 {id:'contract', text:'For a standard U.S. fixed-rate mortgage, you signed a contract with a set interest rate.', caption:'Your rate is set in the contract.'},
 {id:'policy', text:'That rate does not reset when the Fed changes its overnight lending target.', caption:'Policy rate ≠ your contract rate.'},
 {id:'chart', text:'Your scheduled principal-and-interest payment stays flat, even if market rates fall.', caption:'Scheduled principal + interest stay flat.'},
 {id:'refinance', text:'Refinancing replaces that old mortgage with a new loan. It is a separate decision,', caption:'Refinancing means a new loan.'},
 {id:'costs', text:'with approval, closing costs, and a new term to compare.', caption:'Compare approval, costs and term.'},
 {id:'escrow', text:'One catch: taxes and insurance can still change your total monthly bill.', caption:'Taxes and insurance can change.'},
 {id:'ending', text:'A rate cut changes the backdrop. It does not rewrite your contract.', caption:'A rate cut does not rewrite your contract.'},
] as const;
