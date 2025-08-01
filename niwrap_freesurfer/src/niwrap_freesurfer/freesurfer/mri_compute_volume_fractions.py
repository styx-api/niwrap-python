# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_COMPUTE_VOLUME_FRACTIONS_METADATA = Metadata(
    id="c96073b430ac3150fa69b6683b53f6001b13902e.boutiques",
    name="mri_compute_volume_fractions",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MriComputeVolumeFractionsParameters = typing.TypedDict('MriComputeVolumeFractionsParameters', {
    "__STYXTYPE__": typing.Literal["mri_compute_volume_fractions"],
    "output_stem": str,
    "registration_file": typing.NotRequired[InputPathType | None],
    "regheader": typing.NotRequired[str | None],
    "usf": typing.NotRequired[float | None],
    "resolution": typing.NotRequired[float | None],
    "resmm": typing.NotRequired[float | None],
    "segmentation_file": typing.NotRequired[InputPathType | None],
    "wsurf": typing.NotRequired[str | None],
    "psurf": typing.NotRequired[str | None],
    "no_aseg": bool,
    "stackfile": typing.NotRequired[str | None],
    "gmfile": typing.NotRequired[str | None],
    "no_fill_csf": bool,
    "dilation": typing.NotRequired[float | None],
    "out_seg": typing.NotRequired[str | None],
    "ttseg": typing.NotRequired[str | None],
    "ttseg_ctab": typing.NotRequired[str | None],
    "mgz_format": bool,
    "mgh_format": bool,
    "nii_format": bool,
    "nii_gz_format": bool,
    "ttype_head": bool,
    "vg_thresh": typing.NotRequired[float | None],
    "debug": bool,
    "checkopts": bool,
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
        "mri_compute_volume_fractions": mri_compute_volume_fractions_cargs,
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
        "mri_compute_volume_fractions": mri_compute_volume_fractions_outputs,
    }.get(t)


class MriComputeVolumeFractionsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_compute_volume_fractions(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_cortex: OutputPathType
    """Output cortex volume file."""
    output_subcort_gm: OutputPathType
    """Output subcortical gray matter volume file."""
    output_wm: OutputPathType
    """Output white matter volume file."""
    output_csf: OutputPathType
    """Output cerebrospinal fluid volume file."""


def mri_compute_volume_fractions_params(
    output_stem: str,
    registration_file: InputPathType | None = None,
    regheader: str | None = None,
    usf: float | None = None,
    resolution: float | None = None,
    resmm: float | None = None,
    segmentation_file: InputPathType | None = None,
    wsurf: str | None = None,
    psurf: str | None = None,
    no_aseg: bool = False,
    stackfile: str | None = None,
    gmfile: str | None = None,
    no_fill_csf: bool = False,
    dilation: float | None = None,
    out_seg: str | None = None,
    ttseg: str | None = None,
    ttseg_ctab: str | None = None,
    mgz_format: bool = False,
    mgh_format: bool = False,
    nii_format: bool = False,
    nii_gz_format: bool = False,
    ttype_head: bool = False,
    vg_thresh: float | None = None,
    debug: bool = False,
    checkopts: bool = False,
) -> MriComputeVolumeFractionsParameters:
    """
    Build parameters.
    
    Args:
        output_stem: Output stem for generated files (e.g. cortex, subcort_gm,\
            wm, csf). Files will be saved with this stem in different formats based\
            on the selected flags.
        registration_file: Registration file (can be LTA or reg.dat). If using\
            reg.dat, a template volume is needed.
        regheader: Specify the subject for regheader.
        usf: Set anatomical upsample factor (default is 2).
        resolution: Resolution setting. Sets USF to round(1/res).
        resmm: Set functional upsampling resolution (default is\
            aseg->xsize/(USF)).
        segmentation_file: Use specified segmentation file instead of aseg.mgz.
        wsurf: Specify the white surface (default is 'white').
        psurf: Specify the pial surface (default is 'pial').
        no_aseg: Do not include aseg in processing (useful for testing).
        stackfile: Put cortex, subcortical GM, WM, CSF into a single\
            multi-frame file.
        gmfile: Put cortex + subcortical GM into a single-frame file.
        no_fill_csf: Do not attempt to fill voxels surrounding segmentation\
            with extracerebral CSF segmentation.
        dilation: For xCSF fill, dilate by specified number (default is 3). Use\
            -1 to fill the entire volume.
        out_seg: Save segmentation (after adding xCSF voxels).
        ttseg: Save tissue type segmentation.
        ttseg_ctab: Save tissue type segmentation color table.
        mgz_format: Use MGZ format.
        mgh_format: Use MGH format.
        nii_format: Use NII format.
        nii_gz_format: Use NII.GZ format.
        ttype_head: Use default+head instead of default tissue type info for\
            segmentation.
        vg_thresh: Threshold for 'ERROR: LTAconcat(): LTAs 0 and 1 do not\
            match'.
        debug: Turn on debugging mode.
        checkopts: Do not run anything, just check options and exit.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_compute_volume_fractions",
        "output_stem": output_stem,
        "no_aseg": no_aseg,
        "no_fill_csf": no_fill_csf,
        "mgz_format": mgz_format,
        "mgh_format": mgh_format,
        "nii_format": nii_format,
        "nii_gz_format": nii_gz_format,
        "ttype_head": ttype_head,
        "debug": debug,
        "checkopts": checkopts,
    }
    if registration_file is not None:
        params["registration_file"] = registration_file
    if regheader is not None:
        params["regheader"] = regheader
    if usf is not None:
        params["usf"] = usf
    if resolution is not None:
        params["resolution"] = resolution
    if resmm is not None:
        params["resmm"] = resmm
    if segmentation_file is not None:
        params["segmentation_file"] = segmentation_file
    if wsurf is not None:
        params["wsurf"] = wsurf
    if psurf is not None:
        params["psurf"] = psurf
    if stackfile is not None:
        params["stackfile"] = stackfile
    if gmfile is not None:
        params["gmfile"] = gmfile
    if dilation is not None:
        params["dilation"] = dilation
    if out_seg is not None:
        params["out_seg"] = out_seg
    if ttseg is not None:
        params["ttseg"] = ttseg
    if ttseg_ctab is not None:
        params["ttseg_ctab"] = ttseg_ctab
    if vg_thresh is not None:
        params["vg_thresh"] = vg_thresh
    return params


def mri_compute_volume_fractions_cargs(
    params: MriComputeVolumeFractionsParameters,
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
    cargs.append("mri_compute_volume_fractions")
    cargs.extend([
        "--o",
        params.get("output_stem")
    ])
    if params.get("registration_file") is not None:
        cargs.extend([
            "--reg",
            execution.input_file(params.get("registration_file"))
        ])
    if params.get("regheader") is not None:
        cargs.extend([
            "--regheader",
            params.get("regheader")
        ])
    if params.get("usf") is not None:
        cargs.extend([
            "--usf",
            str(params.get("usf"))
        ])
    if params.get("resolution") is not None:
        cargs.extend([
            "--r",
            str(params.get("resolution"))
        ])
    if params.get("resmm") is not None:
        cargs.extend([
            "--resmm",
            str(params.get("resmm"))
        ])
    if params.get("segmentation_file") is not None:
        cargs.extend([
            "--seg",
            execution.input_file(params.get("segmentation_file"))
        ])
    if params.get("wsurf") is not None:
        cargs.extend([
            "--wsurf",
            params.get("wsurf")
        ])
    if params.get("psurf") is not None:
        cargs.extend([
            "--psurf",
            params.get("psurf")
        ])
    if params.get("no_aseg"):
        cargs.append("--no-aseg")
    if params.get("stackfile") is not None:
        cargs.extend([
            "--stack",
            params.get("stackfile")
        ])
    if params.get("gmfile") is not None:
        cargs.extend([
            "--gm",
            params.get("gmfile")
        ])
    if params.get("no_fill_csf"):
        cargs.append("--no-fill-csf")
    if params.get("dilation") is not None:
        cargs.extend([
            "--dil",
            str(params.get("dilation"))
        ])
    if params.get("out_seg") is not None:
        cargs.extend([
            "--out-seg",
            params.get("out_seg")
        ])
    if params.get("ttseg") is not None:
        cargs.extend([
            "--ttseg",
            params.get("ttseg")
        ])
    if params.get("ttseg_ctab") is not None:
        cargs.extend([
            "--ttseg-ctab",
            params.get("ttseg_ctab")
        ])
    if params.get("mgz_format"):
        cargs.append("--mgz")
    if params.get("mgh_format"):
        cargs.append("--mgh")
    if params.get("nii_format"):
        cargs.append("--nii")
    if params.get("nii_gz_format"):
        cargs.append("--nii.gz")
    if params.get("ttype_head"):
        cargs.append("--ttype+head")
    if params.get("vg_thresh") is not None:
        cargs.extend([
            "--vg-thresh",
            str(params.get("vg_thresh"))
        ])
    if params.get("debug"):
        cargs.append("--debug")
    if params.get("checkopts"):
        cargs.append("--checkopts")
    return cargs


def mri_compute_volume_fractions_outputs(
    params: MriComputeVolumeFractionsParameters,
    execution: Execution,
) -> MriComputeVolumeFractionsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriComputeVolumeFractionsOutputs(
        root=execution.output_file("."),
        output_cortex=execution.output_file(params.get("output_stem") + ".cortex.mgz"),
        output_subcort_gm=execution.output_file(params.get("output_stem") + ".subcort_gm.mgz"),
        output_wm=execution.output_file(params.get("output_stem") + ".wm.mgz"),
        output_csf=execution.output_file(params.get("output_stem") + ".csf.mgz"),
    )
    return ret


def mri_compute_volume_fractions_execute(
    params: MriComputeVolumeFractionsParameters,
    execution: Execution,
) -> MriComputeVolumeFractionsOutputs:
    """
    Computes partial volume fractions for cortex, subcortical GM, WM and CSF.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriComputeVolumeFractionsOutputs`).
    """
    params = execution.params(params)
    cargs = mri_compute_volume_fractions_cargs(params, execution)
    ret = mri_compute_volume_fractions_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_compute_volume_fractions(
    output_stem: str,
    registration_file: InputPathType | None = None,
    regheader: str | None = None,
    usf: float | None = None,
    resolution: float | None = None,
    resmm: float | None = None,
    segmentation_file: InputPathType | None = None,
    wsurf: str | None = None,
    psurf: str | None = None,
    no_aseg: bool = False,
    stackfile: str | None = None,
    gmfile: str | None = None,
    no_fill_csf: bool = False,
    dilation: float | None = None,
    out_seg: str | None = None,
    ttseg: str | None = None,
    ttseg_ctab: str | None = None,
    mgz_format: bool = False,
    mgh_format: bool = False,
    nii_format: bool = False,
    nii_gz_format: bool = False,
    ttype_head: bool = False,
    vg_thresh: float | None = None,
    debug: bool = False,
    checkopts: bool = False,
    runner: Runner | None = None,
) -> MriComputeVolumeFractionsOutputs:
    """
    Computes partial volume fractions for cortex, subcortical GM, WM and CSF.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        output_stem: Output stem for generated files (e.g. cortex, subcort_gm,\
            wm, csf). Files will be saved with this stem in different formats based\
            on the selected flags.
        registration_file: Registration file (can be LTA or reg.dat). If using\
            reg.dat, a template volume is needed.
        regheader: Specify the subject for regheader.
        usf: Set anatomical upsample factor (default is 2).
        resolution: Resolution setting. Sets USF to round(1/res).
        resmm: Set functional upsampling resolution (default is\
            aseg->xsize/(USF)).
        segmentation_file: Use specified segmentation file instead of aseg.mgz.
        wsurf: Specify the white surface (default is 'white').
        psurf: Specify the pial surface (default is 'pial').
        no_aseg: Do not include aseg in processing (useful for testing).
        stackfile: Put cortex, subcortical GM, WM, CSF into a single\
            multi-frame file.
        gmfile: Put cortex + subcortical GM into a single-frame file.
        no_fill_csf: Do not attempt to fill voxels surrounding segmentation\
            with extracerebral CSF segmentation.
        dilation: For xCSF fill, dilate by specified number (default is 3). Use\
            -1 to fill the entire volume.
        out_seg: Save segmentation (after adding xCSF voxels).
        ttseg: Save tissue type segmentation.
        ttseg_ctab: Save tissue type segmentation color table.
        mgz_format: Use MGZ format.
        mgh_format: Use MGH format.
        nii_format: Use NII format.
        nii_gz_format: Use NII.GZ format.
        ttype_head: Use default+head instead of default tissue type info for\
            segmentation.
        vg_thresh: Threshold for 'ERROR: LTAconcat(): LTAs 0 and 1 do not\
            match'.
        debug: Turn on debugging mode.
        checkopts: Do not run anything, just check options and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriComputeVolumeFractionsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_COMPUTE_VOLUME_FRACTIONS_METADATA)
    params = mri_compute_volume_fractions_params(
        output_stem=output_stem,
        registration_file=registration_file,
        regheader=regheader,
        usf=usf,
        resolution=resolution,
        resmm=resmm,
        segmentation_file=segmentation_file,
        wsurf=wsurf,
        psurf=psurf,
        no_aseg=no_aseg,
        stackfile=stackfile,
        gmfile=gmfile,
        no_fill_csf=no_fill_csf,
        dilation=dilation,
        out_seg=out_seg,
        ttseg=ttseg,
        ttseg_ctab=ttseg_ctab,
        mgz_format=mgz_format,
        mgh_format=mgh_format,
        nii_format=nii_format,
        nii_gz_format=nii_gz_format,
        ttype_head=ttype_head,
        vg_thresh=vg_thresh,
        debug=debug,
        checkopts=checkopts,
    )
    return mri_compute_volume_fractions_execute(params, execution)


__all__ = [
    "MRI_COMPUTE_VOLUME_FRACTIONS_METADATA",
    "MriComputeVolumeFractionsOutputs",
    "MriComputeVolumeFractionsParameters",
    "mri_compute_volume_fractions",
    "mri_compute_volume_fractions_params",
]
