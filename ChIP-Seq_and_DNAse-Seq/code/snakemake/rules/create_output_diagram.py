rule create_output_diagram:
    input: "RESULTS/OUTPUT/table_summary_stats.txt"
    output: "RESULTS/OUTPUT/table_summary_stats.pdf"
    params: ppn="nodes=1:ppn=1"
    run: R("""
    d <- read.table("{input}", sep="\t", head=F)
    d <- d[d[,1] =="Binomial_test",]
    pval <- d[d[,1] =="Binomial_test",2]
    d <- d[order(pval),]
    mark <- unlist(lapply(strsplit(basename(as.character(d$V3)), "_"), "[", 5))
    control.or.not <- unlist(lapply(strsplit(basename(as.character(d$V3)), "-"), "[", 1))  
    cn <-   control.or.not
    control.or.not <- as.factor(control.or.not)
    levels(control.or.not) <- c("blue","darkgrey")
    control.or.not <- as.character(control.or.not)
    pval <- d[,2]
   
    pdf("{output}")
    par(mar = c(7, 4, 2, 2) + 0.2)
    x <- barplot(-log10(pval), border=NA, col=control.or.not, las=2, ylab="-log10(binomial test p-value)", xlab="ChIA-PET, target", xaxt="n") 
    text(x=x+0.5, y=-0.25, mark, xpd=TRUE, srt=45, pos=2, cex=0.5)
    text(x=x, y=-log10(pval)+0.5, cn , xpd=TRUE,srt=90, cex=0.5)
    abline(h=-log10(0.05), lty=2, col="red")
    out <- dev.off()
    
    """)
