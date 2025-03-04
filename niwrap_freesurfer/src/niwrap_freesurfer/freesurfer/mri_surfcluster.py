# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_SURFCLUSTER_METADATA = Metadata(
    id="d511292684dbbb10f74daadd0e2a8026a7360392.boutiques",
    name="mri_surfcluster",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MriSurfclusterParameters = typing.TypedDict('MriSurfclusterParameters', {
    "__STYX_TYPE__": typing.Literal["mri_surfcluster"],
    "infile": InputPathType,
    "thmin": typing.NotRequired[float | None],
    "sign": typing.NotRequired[str | None],
    "no_adjust_flag": bool,
    "fdr": typing.NotRequired[float | None],
    "subject": typing.NotRequired[str | None],
    "hemi": typing.NotRequired[str | None],
    "surf": typing.NotRequired[str | None],
    "surfpath": typing.NotRequired[str | None],
    "annot": typing.NotRequired[str | None],
    "frame": typing.NotRequired[float | None],
    "csd": typing.NotRequired[list[InputPathType] | None],
    "vwsig": typing.NotRequired[str | None],
    "cwsig": typing.NotRequired[str | None],
    "maxcwpval": typing.NotRequired[str | None],
    "bonferroni": typing.NotRequired[float | None],
    "sig2p_max_flag": bool,
    "bonferroni_max": typing.NotRequired[float | None],
    "csdpdf": typing.NotRequired[str | None],
    "csdpdf_only_flag": bool,
    "csd_out": typing.NotRequired[InputPathType | None],
    "cwpvalthresh": typing.NotRequired[float | None],
    "fwhm": typing.NotRequired[float | None],
    "fwhmdat": typing.NotRequired[str | None],
    "clabel": typing.NotRequired[InputPathType | None],
    "cortex_flag": bool,
    "mask": typing.NotRequired[InputPathType | None],
    "mask_inv_flag": bool,
    "centroid_flag": bool,
    "sum": typing.NotRequired[InputPathType | None],
    "pointset": typing.NotRequired[InputPathType | None],
    "maxareafile": typing.NotRequired[str | None],
    "o": typing.NotRequired[str | None],
    "ocn": typing.NotRequired[str | None],
    "olab": typing.NotRequired[str | None],
    "oannot": typing.NotRequired[str | None],
    "minarea": typing.NotRequired[float | None],
    "xfm": typing.NotRequired[InputPathType | None],
    "no_fixmni_flag": bool,
    "sd": typing.NotRequired[str | None],
    "thmax": typing.NotRequired[float | None],
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "mri_surfcluster": mri_surfcluster_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
        "mri_surfcluster": mri_surfcluster_outputs,
    }.get(t)


class MriSurfclusterOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_surfcluster(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_surface_file: OutputPathType | None
    """Filtered surface file with non-cluster vertices set to 0"""
    output_cluster_number_file: OutputPathType | None
    """Surface file with cluster number per vertex"""
    output_labels: OutputPathType | None
    """Label files for clusters"""
    output_summary_file: OutputPathType | None
    """Text summary file of clustering results"""
    output_pointset_file: OutputPathType | None
    """Pointset file for visualization in Freeview"""
    output_max_area_file: OutputPathType | None
    """File containing the area of the largest cluster"""


def mri_surfcluster_params(
    infile: InputPathType,
    thmin: float | None = None,
    sign: str | None = None,
    no_adjust_flag: bool = False,
    fdr: float | None = None,
    subject: str | None = None,
    hemi: str | None = None,
    surf: str | None = None,
    surfpath: str | None = None,
    annot: str | None = None,
    frame: float | None = None,
    csd: list[InputPathType] | None = None,
    vwsig: str | None = None,
    cwsig: str | None = None,
    maxcwpval: str | None = None,
    bonferroni: float | None = None,
    sig2p_max_flag: bool = False,
    bonferroni_max: float | None = None,
    csdpdf: str | None = None,
    csdpdf_only_flag: bool = False,
    csd_out: InputPathType | None = None,
    cwpvalthresh: float | None = None,
    fwhm: float | None = None,
    fwhmdat: str | None = None,
    clabel: InputPathType | None = None,
    cortex_flag: bool = False,
    mask: InputPathType | None = None,
    mask_inv_flag: bool = False,
    centroid_flag: bool = False,
    sum_: InputPathType | None = None,
    pointset: InputPathType | None = None,
    maxareafile: str | None = None,
    o: str | None = None,
    ocn: str | None = None,
    olab: str | None = None,
    oannot: str | None = None,
    minarea: float | None = None,
    xfm: InputPathType | None = None,
    no_fixmni_flag: bool = False,
    sd: str | None = None,
    thmax: float | None = None,
) -> MriSurfclusterParameters:
    """
    Build parameters.
    
    Args:
        infile: Source of surface values.
        thmin: Minimum intensity threshold.
        sign: Sign of threshold criteria (abs, pos, neg).
        no_adjust_flag: Do not adjust threshold for one-tailed tests.
        fdr: Set thmin with False Discovery Rate.
        subject: Source surface subject (can be ico).
        hemi: Cortical hemisphere, either lh or rh.
        surf: Coordinates from surface (e.g., white).
        surfpath: Full path to surface.
        annot: Report annotation for max vertex (e.g., aparc).
        frame: 0-based frame number of the input file.
        csd: Load one or more CSD files.
        vwsig: Map of corrected voxel-wise significances.
        cwsig: Map of cluster-wise significances.
        maxcwpval: Save p-value of the largest (max) cluster.
        bonferroni: Apply Bonferroni correction across N spaces.
        sig2p_max_flag: Convert max from sig to p.
        bonferroni_max: Apply Bonferroni correction to maximum.
        csdpdf: Compute PDF/CDF of CSD data and save.
        csdpdf_only_flag: Only write the CSD PDF file.
        csd_out: Write out merged CSD files as one.
        cwpvalthresh: Cluster-wise threshold.
        fwhm: FWHM in mm^2 for GRF.
        fwhmdat: Text file with FWHM in mm^2 for GRF.
        clabel: Constrain cluster search to be inside or outside clabel.
        cortex_flag: Set clabel to be subject/label/hemi.cortex.label.
        mask: Constrain to be within mask.
        mask_inv_flag: Constrain cluster search to be outside mask or clabel.
        centroid_flag: Report centroid instead of location of maximum stat.
        sum_: Text file to store cluster summary.
        pointset: File that can be read into Freeview with -c.
        maxareafile: Write area of largest cluster to this file.
        o: Output file with non-clusters set to 0.
        ocn: Output file where value is cluster number.
        olab: Output clusters as labels.
        oannot: Output clusters as an annotation.
        minarea: Area threshold for a cluster (mm^2).
        xfm: Talairach transform file.
        no_fixmni_flag: Do not fix MNI Talairach coordinates.
        sd: FreeSurfer subjects directory.
        thmax: Maximum intensity threshold.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_surfcluster",
        "infile": infile,
        "no_adjust_flag": no_adjust_flag,
        "sig2p_max_flag": sig2p_max_flag,
        "csdpdf_only_flag": csdpdf_only_flag,
        "cortex_flag": cortex_flag,
        "mask_inv_flag": mask_inv_flag,
        "centroid_flag": centroid_flag,
        "no_fixmni_flag": no_fixmni_flag,
    }
    if thmin is not None:
        params["thmin"] = thmin
    if sign is not None:
        params["sign"] = sign
    if fdr is not None:
        params["fdr"] = fdr
    if subject is not None:
        params["subject"] = subject
    if hemi is not None:
        params["hemi"] = hemi
    if surf is not None:
        params["surf"] = surf
    if surfpath is not None:
        params["surfpath"] = surfpath
    if annot is not None:
        params["annot"] = annot
    if frame is not None:
        params["frame"] = frame
    if csd is not None:
        params["csd"] = csd
    if vwsig is not None:
        params["vwsig"] = vwsig
    if cwsig is not None:
        params["cwsig"] = cwsig
    if maxcwpval is not None:
        params["maxcwpval"] = maxcwpval
    if bonferroni is not None:
        params["bonferroni"] = bonferroni
    if bonferroni_max is not None:
        params["bonferroni_max"] = bonferroni_max
    if csdpdf is not None:
        params["csdpdf"] = csdpdf
    if csd_out is not None:
        params["csd_out"] = csd_out
    if cwpvalthresh is not None:
        params["cwpvalthresh"] = cwpvalthresh
    if fwhm is not None:
        params["fwhm"] = fwhm
    if fwhmdat is not None:
        params["fwhmdat"] = fwhmdat
    if clabel is not None:
        params["clabel"] = clabel
    if mask is not None:
        params["mask"] = mask
    if sum_ is not None:
        params["sum"] = sum_
    if pointset is not None:
        params["pointset"] = pointset
    if maxareafile is not None:
        params["maxareafile"] = maxareafile
    if o is not None:
        params["o"] = o
    if ocn is not None:
        params["ocn"] = ocn
    if olab is not None:
        params["olab"] = olab
    if oannot is not None:
        params["oannot"] = oannot
    if minarea is not None:
        params["minarea"] = minarea
    if xfm is not None:
        params["xfm"] = xfm
    if sd is not None:
        params["sd"] = sd
    if thmax is not None:
        params["thmax"] = thmax
    return params


def mri_surfcluster_cargs(
    params: MriSurfclusterParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("mri_surfcluster")
    cargs.extend([
        "--in",
        execution.input_file(params.get("infile"))
    ])
    if params.get("thmin") is not None:
        cargs.extend([
            "--thmin",
            str(params.get("thmin"))
        ])
    if params.get("sign") is not None:
        cargs.extend([
            "--sign",
            params.get("sign")
        ])
    if params.get("no_adjust_flag"):
        cargs.append("--no-adjust")
    if params.get("fdr") is not None:
        cargs.extend([
            "--fdr",
            str(params.get("fdr"))
        ])
    if params.get("subject") is not None:
        cargs.extend([
            "--subject",
            params.get("subject")
        ])
    if params.get("hemi") is not None:
        cargs.extend([
            "--hemi",
            params.get("hemi")
        ])
    if params.get("surf") is not None:
        cargs.extend([
            "--surf",
            params.get("surf")
        ])
    if params.get("surfpath") is not None:
        cargs.extend([
            "--surfpath",
            params.get("surfpath")
        ])
    if params.get("annot") is not None:
        cargs.extend([
            "--annot",
            params.get("annot")
        ])
    if params.get("frame") is not None:
        cargs.extend([
            "--frame",
            str(params.get("frame"))
        ])
    if params.get("csd") is not None:
        cargs.extend([
            "--csd",
            *[execution.input_file(f) for f in params.get("csd")]
        ])
    if params.get("vwsig") is not None:
        cargs.extend([
            "--vwsig",
            params.get("vwsig")
        ])
    if params.get("cwsig") is not None:
        cargs.extend([
            "--cwsig",
            params.get("cwsig")
        ])
    if params.get("maxcwpval") is not None:
        cargs.extend([
            "--maxcwpval",
            params.get("maxcwpval")
        ])
    if params.get("bonferroni") is not None:
        cargs.extend([
            "--bonferroni",
            str(params.get("bonferroni"))
        ])
    if params.get("sig2p_max_flag"):
        cargs.append("--sig2p-max")
    if params.get("bonferroni_max") is not None:
        cargs.extend([
            "--bonferroni-max",
            str(params.get("bonferroni_max"))
        ])
    if params.get("csdpdf") is not None:
        cargs.extend([
            "--csdpdf",
            params.get("csdpdf")
        ])
    if params.get("csdpdf_only_flag"):
        cargs.append("--csdpdf-only")
    if params.get("csd_out") is not None:
        cargs.extend([
            "--csd-out",
            execution.input_file(params.get("csd_out"))
        ])
    if params.get("cwpvalthresh") is not None:
        cargs.extend([
            "--cwpvalthresh",
            str(params.get("cwpvalthresh"))
        ])
    if params.get("fwhm") is not None:
        cargs.extend([
            "--fwhm",
            str(params.get("fwhm"))
        ])
    if params.get("fwhmdat") is not None:
        cargs.extend([
            "--fwhmdat",
            params.get("fwhmdat")
        ])
    if params.get("clabel") is not None:
        cargs.extend([
            "--clabel",
            execution.input_file(params.get("clabel"))
        ])
    if params.get("cortex_flag"):
        cargs.append("--cortex")
    if params.get("mask") is not None:
        cargs.extend([
            "--mask",
            execution.input_file(params.get("mask"))
        ])
    if params.get("mask_inv_flag"):
        cargs.append("--mask-inv")
    if params.get("centroid_flag"):
        cargs.append("--centroid")
    if params.get("sum") is not None:
        cargs.extend([
            "--sum",
            execution.input_file(params.get("sum"))
        ])
    if params.get("pointset") is not None:
        cargs.extend([
            "--pointset",
            execution.input_file(params.get("pointset"))
        ])
    if params.get("maxareafile") is not None:
        cargs.extend([
            "--maxareafile",
            params.get("maxareafile")
        ])
    if params.get("o") is not None:
        cargs.extend([
            "--o",
            params.get("o")
        ])
    if params.get("ocn") is not None:
        cargs.extend([
            "--ocn",
            params.get("ocn")
        ])
    if params.get("olab") is not None:
        cargs.extend([
            "--olab",
            params.get("olab")
        ])
    if params.get("oannot") is not None:
        cargs.extend([
            "--oannot",
            params.get("oannot")
        ])
    if params.get("minarea") is not None:
        cargs.extend([
            "--minarea",
            str(params.get("minarea"))
        ])
    if params.get("xfm") is not None:
        cargs.extend([
            "--xfm",
            execution.input_file(params.get("xfm"))
        ])
    if params.get("no_fixmni_flag"):
        cargs.append("--nofixmni")
    if params.get("sd") is not None:
        cargs.extend([
            "--sd",
            params.get("sd")
        ])
    if params.get("thmax") is not None:
        cargs.extend([
            "--thmax",
            str(params.get("thmax"))
        ])
    return cargs


def mri_surfcluster_outputs(
    params: MriSurfclusterParameters,
    execution: Execution,
) -> MriSurfclusterOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriSurfclusterOutputs(
        root=execution.output_file("."),
        output_surface_file=execution.output_file(params.get("o")) if (params.get("o") is not None) else None,
        output_cluster_number_file=execution.output_file(params.get("ocn")) if (params.get("ocn") is not None) else None,
        output_labels=execution.output_file(params.get("olab") + "-*.label") if (params.get("olab") is not None) else None,
        output_summary_file=execution.output_file(pathlib.Path(params.get("sum")).name) if (params.get("sum") is not None) else None,
        output_pointset_file=execution.output_file(pathlib.Path(params.get("pointset")).name) if (params.get("pointset") is not None) else None,
        output_max_area_file=execution.output_file(params.get("maxareafile")) if (params.get("maxareafile") is not None) else None,
    )
    return ret


def mri_surfcluster_execute(
    params: MriSurfclusterParameters,
    execution: Execution,
) -> MriSurfclusterOutputs:
    """
    A tool for clustering vertices on a cortical surface based on intensity values.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriSurfclusterOutputs`).
    """
    params = execution.params(params)
    cargs = mri_surfcluster_cargs(params, execution)
    ret = mri_surfcluster_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_surfcluster(
    infile: InputPathType,
    thmin: float | None = None,
    sign: str | None = None,
    no_adjust_flag: bool = False,
    fdr: float | None = None,
    subject: str | None = None,
    hemi: str | None = None,
    surf: str | None = None,
    surfpath: str | None = None,
    annot: str | None = None,
    frame: float | None = None,
    csd: list[InputPathType] | None = None,
    vwsig: str | None = None,
    cwsig: str | None = None,
    maxcwpval: str | None = None,
    bonferroni: float | None = None,
    sig2p_max_flag: bool = False,
    bonferroni_max: float | None = None,
    csdpdf: str | None = None,
    csdpdf_only_flag: bool = False,
    csd_out: InputPathType | None = None,
    cwpvalthresh: float | None = None,
    fwhm: float | None = None,
    fwhmdat: str | None = None,
    clabel: InputPathType | None = None,
    cortex_flag: bool = False,
    mask: InputPathType | None = None,
    mask_inv_flag: bool = False,
    centroid_flag: bool = False,
    sum_: InputPathType | None = None,
    pointset: InputPathType | None = None,
    maxareafile: str | None = None,
    o: str | None = None,
    ocn: str | None = None,
    olab: str | None = None,
    oannot: str | None = None,
    minarea: float | None = None,
    xfm: InputPathType | None = None,
    no_fixmni_flag: bool = False,
    sd: str | None = None,
    thmax: float | None = None,
    runner: Runner | None = None,
) -> MriSurfclusterOutputs:
    """
    A tool for clustering vertices on a cortical surface based on intensity values.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        infile: Source of surface values.
        thmin: Minimum intensity threshold.
        sign: Sign of threshold criteria (abs, pos, neg).
        no_adjust_flag: Do not adjust threshold for one-tailed tests.
        fdr: Set thmin with False Discovery Rate.
        subject: Source surface subject (can be ico).
        hemi: Cortical hemisphere, either lh or rh.
        surf: Coordinates from surface (e.g., white).
        surfpath: Full path to surface.
        annot: Report annotation for max vertex (e.g., aparc).
        frame: 0-based frame number of the input file.
        csd: Load one or more CSD files.
        vwsig: Map of corrected voxel-wise significances.
        cwsig: Map of cluster-wise significances.
        maxcwpval: Save p-value of the largest (max) cluster.
        bonferroni: Apply Bonferroni correction across N spaces.
        sig2p_max_flag: Convert max from sig to p.
        bonferroni_max: Apply Bonferroni correction to maximum.
        csdpdf: Compute PDF/CDF of CSD data and save.
        csdpdf_only_flag: Only write the CSD PDF file.
        csd_out: Write out merged CSD files as one.
        cwpvalthresh: Cluster-wise threshold.
        fwhm: FWHM in mm^2 for GRF.
        fwhmdat: Text file with FWHM in mm^2 for GRF.
        clabel: Constrain cluster search to be inside or outside clabel.
        cortex_flag: Set clabel to be subject/label/hemi.cortex.label.
        mask: Constrain to be within mask.
        mask_inv_flag: Constrain cluster search to be outside mask or clabel.
        centroid_flag: Report centroid instead of location of maximum stat.
        sum_: Text file to store cluster summary.
        pointset: File that can be read into Freeview with -c.
        maxareafile: Write area of largest cluster to this file.
        o: Output file with non-clusters set to 0.
        ocn: Output file where value is cluster number.
        olab: Output clusters as labels.
        oannot: Output clusters as an annotation.
        minarea: Area threshold for a cluster (mm^2).
        xfm: Talairach transform file.
        no_fixmni_flag: Do not fix MNI Talairach coordinates.
        sd: FreeSurfer subjects directory.
        thmax: Maximum intensity threshold.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriSurfclusterOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_SURFCLUSTER_METADATA)
    params = mri_surfcluster_params(
        infile=infile,
        thmin=thmin,
        sign=sign,
        no_adjust_flag=no_adjust_flag,
        fdr=fdr,
        subject=subject,
        hemi=hemi,
        surf=surf,
        surfpath=surfpath,
        annot=annot,
        frame=frame,
        csd=csd,
        vwsig=vwsig,
        cwsig=cwsig,
        maxcwpval=maxcwpval,
        bonferroni=bonferroni,
        sig2p_max_flag=sig2p_max_flag,
        bonferroni_max=bonferroni_max,
        csdpdf=csdpdf,
        csdpdf_only_flag=csdpdf_only_flag,
        csd_out=csd_out,
        cwpvalthresh=cwpvalthresh,
        fwhm=fwhm,
        fwhmdat=fwhmdat,
        clabel=clabel,
        cortex_flag=cortex_flag,
        mask=mask,
        mask_inv_flag=mask_inv_flag,
        centroid_flag=centroid_flag,
        sum_=sum_,
        pointset=pointset,
        maxareafile=maxareafile,
        o=o,
        ocn=ocn,
        olab=olab,
        oannot=oannot,
        minarea=minarea,
        xfm=xfm,
        no_fixmni_flag=no_fixmni_flag,
        sd=sd,
        thmax=thmax,
    )
    return mri_surfcluster_execute(params, execution)


__all__ = [
    "MRI_SURFCLUSTER_METADATA",
    "MriSurfclusterOutputs",
    "MriSurfclusterParameters",
    "mri_surfcluster",
    "mri_surfcluster_params",
]
