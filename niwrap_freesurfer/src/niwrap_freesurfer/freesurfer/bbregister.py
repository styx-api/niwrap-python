# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

BBREGISTER_METADATA = Metadata(
    id="5afef238c6734753905291f538bd2eab731681c0.boutiques",
    name="bbregister",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


BbregisterParameters = typing.TypedDict('BbregisterParameters', {
    "__STYXTYPE__": typing.Literal["bbregister"],
    "subject": str,
    "moveable_volume": InputPathType,
    "reg_file": str,
    "contrast_type_t1": bool,
    "contrast_type_t2": bool,
    "vsm": typing.NotRequired[InputPathType | None],
    "init_coreg": bool,
    "no_coreg_ref_mask": bool,
    "init_header": bool,
    "init_reg": typing.NotRequired[InputPathType | None],
    "intvol": typing.NotRequired[InputPathType | None],
    "mid_frame": bool,
    "frame_no": typing.NotRequired[float | None],
    "template_out": typing.NotRequired[str | None],
    "o_outvol": typing.NotRequired[str | None],
    "s_from_reg": bool,
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
        "bbregister": bbregister_cargs,
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
        "bbregister": bbregister_outputs,
    }.get(t)


class BbregisterOutputs(typing.NamedTuple):
    """
    Output object returned when calling `bbregister(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    reg_output: OutputPathType
    """Output registration file in dat or lta format."""
    out_volume: OutputPathType | None
    """Resampled moveable volume."""


def bbregister_params(
    subject: str,
    moveable_volume: InputPathType,
    reg_file: str,
    contrast_type_t1: bool = False,
    contrast_type_t2: bool = False,
    vsm: InputPathType | None = None,
    init_coreg: bool = False,
    no_coreg_ref_mask: bool = False,
    init_header: bool = False,
    init_reg: InputPathType | None = None,
    intvol: InputPathType | None = None,
    mid_frame: bool = False,
    frame_no: float | None = None,
    template_out: str | None = None,
    o_outvol: str | None = None,
    s_from_reg: bool = False,
) -> BbregisterParameters:
    """
    Build parameters.
    
    Args:
        subject: FreeSurfer subject name as found in $SUBJECTS_DIR.
        moveable_volume: "Moveable" volume template for cross-modal volume.\
            E.g., fMRI volume used for motion correction.
        reg_file: Output FreeSurfer registration file (tkregister-style or LTA\
            format).
        contrast_type_t1: Assume T1 contrast, White Matter brighter than Grey\
            Matter.
        contrast_type_t2: Assume T2 contrast, Grey Matter brighter than White\
            Matter. Same as --bold and --dti.
        vsm: Include B0 distortion correction. A voxel shift map can be created\
            with the epidewarp.fsl script.
        init_coreg: Initialize with FreeSurfer mri_coreg program.
        no_coreg_ref_mask: Do not use aparc+aseg.mgz as a reference mask.
        init_header: Use geometry info for close voxel-to-voxel registration.\
            Typically valid if acquired in same session.
        init_reg: Supply an initial registration matrix; can be LTA format.
        intvol: Volume used as an intermediate during registration. Useful for\
            partial field-of-view volumes.
        mid_frame: Register to middle frame (not with --frame option).
        frame_no: Register to specified frame (default is 0=1st).
        template_out: Save template (beneficial with --frame).
        o_outvol: Resample moveable volume and save as specified output volume.
        s_from_reg: Get subject name from registration file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "bbregister",
        "subject": subject,
        "moveable_volume": moveable_volume,
        "reg_file": reg_file,
        "contrast_type_t1": contrast_type_t1,
        "contrast_type_t2": contrast_type_t2,
        "init_coreg": init_coreg,
        "no_coreg_ref_mask": no_coreg_ref_mask,
        "init_header": init_header,
        "mid_frame": mid_frame,
        "s_from_reg": s_from_reg,
    }
    if vsm is not None:
        params["vsm"] = vsm
    if init_reg is not None:
        params["init_reg"] = init_reg
    if intvol is not None:
        params["intvol"] = intvol
    if frame_no is not None:
        params["frame_no"] = frame_no
    if template_out is not None:
        params["template_out"] = template_out
    if o_outvol is not None:
        params["o_outvol"] = o_outvol
    return params


def bbregister_cargs(
    params: BbregisterParameters,
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
    cargs.append("bbregister")
    cargs.extend([
        "--s",
        params.get("subject")
    ])
    cargs.extend([
        "--mov",
        execution.input_file(params.get("moveable_volume"))
    ])
    cargs.extend([
        "--reg",
        params.get("reg_file")
    ])
    if params.get("contrast_type_t1"):
        cargs.append("--t1")
    if params.get("contrast_type_t2"):
        cargs.append("--t2")
    if params.get("vsm") is not None:
        cargs.extend([
            "--vsm",
            execution.input_file(params.get("vsm"))
        ])
    if params.get("init_coreg"):
        cargs.append("--init-coreg")
    if params.get("no_coreg_ref_mask"):
        cargs.append("--no-coreg-ref-mask")
    if params.get("init_header"):
        cargs.append("--init-header")
    if params.get("init_reg") is not None:
        cargs.extend([
            "--init-reg",
            execution.input_file(params.get("init_reg"))
        ])
    if params.get("intvol") is not None:
        cargs.extend([
            "--int",
            execution.input_file(params.get("intvol"))
        ])
    if params.get("mid_frame"):
        cargs.append("--mid-frame")
    if params.get("frame_no") is not None:
        cargs.extend([
            "--frame",
            str(params.get("frame_no"))
        ])
    if params.get("template_out") is not None:
        cargs.extend([
            "--template-out",
            params.get("template_out")
        ])
    if params.get("o_outvol") is not None:
        cargs.extend([
            "--o",
            params.get("o_outvol")
        ])
    if params.get("s_from_reg"):
        cargs.append("--s-from-reg")
    return cargs


def bbregister_outputs(
    params: BbregisterParameters,
    execution: Execution,
) -> BbregisterOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = BbregisterOutputs(
        root=execution.output_file("."),
        reg_output=execution.output_file(params.get("reg_file")),
        out_volume=execution.output_file(params.get("o_outvol")) if (params.get("o_outvol") is not None) else None,
    )
    return ret


def bbregister_execute(
    params: BbregisterParameters,
    execution: Execution,
) -> BbregisterOutputs:
    """
    Performs within-subject, cross-modal registration using a boundary-based cost
    function.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `BbregisterOutputs`).
    """
    params = execution.params(params)
    cargs = bbregister_cargs(params, execution)
    ret = bbregister_outputs(params, execution)
    execution.run(cargs)
    return ret


def bbregister(
    subject: str,
    moveable_volume: InputPathType,
    reg_file: str,
    contrast_type_t1: bool = False,
    contrast_type_t2: bool = False,
    vsm: InputPathType | None = None,
    init_coreg: bool = False,
    no_coreg_ref_mask: bool = False,
    init_header: bool = False,
    init_reg: InputPathType | None = None,
    intvol: InputPathType | None = None,
    mid_frame: bool = False,
    frame_no: float | None = None,
    template_out: str | None = None,
    o_outvol: str | None = None,
    s_from_reg: bool = False,
    runner: Runner | None = None,
) -> BbregisterOutputs:
    """
    Performs within-subject, cross-modal registration using a boundary-based cost
    function.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject: FreeSurfer subject name as found in $SUBJECTS_DIR.
        moveable_volume: "Moveable" volume template for cross-modal volume.\
            E.g., fMRI volume used for motion correction.
        reg_file: Output FreeSurfer registration file (tkregister-style or LTA\
            format).
        contrast_type_t1: Assume T1 contrast, White Matter brighter than Grey\
            Matter.
        contrast_type_t2: Assume T2 contrast, Grey Matter brighter than White\
            Matter. Same as --bold and --dti.
        vsm: Include B0 distortion correction. A voxel shift map can be created\
            with the epidewarp.fsl script.
        init_coreg: Initialize with FreeSurfer mri_coreg program.
        no_coreg_ref_mask: Do not use aparc+aseg.mgz as a reference mask.
        init_header: Use geometry info for close voxel-to-voxel registration.\
            Typically valid if acquired in same session.
        init_reg: Supply an initial registration matrix; can be LTA format.
        intvol: Volume used as an intermediate during registration. Useful for\
            partial field-of-view volumes.
        mid_frame: Register to middle frame (not with --frame option).
        frame_no: Register to specified frame (default is 0=1st).
        template_out: Save template (beneficial with --frame).
        o_outvol: Resample moveable volume and save as specified output volume.
        s_from_reg: Get subject name from registration file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `BbregisterOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(BBREGISTER_METADATA)
    params = bbregister_params(
        subject=subject,
        moveable_volume=moveable_volume,
        reg_file=reg_file,
        contrast_type_t1=contrast_type_t1,
        contrast_type_t2=contrast_type_t2,
        vsm=vsm,
        init_coreg=init_coreg,
        no_coreg_ref_mask=no_coreg_ref_mask,
        init_header=init_header,
        init_reg=init_reg,
        intvol=intvol,
        mid_frame=mid_frame,
        frame_no=frame_no,
        template_out=template_out,
        o_outvol=o_outvol,
        s_from_reg=s_from_reg,
    )
    return bbregister_execute(params, execution)


__all__ = [
    "BBREGISTER_METADATA",
    "BbregisterOutputs",
    "BbregisterParameters",
    "bbregister",
    "bbregister_params",
]
