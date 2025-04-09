# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FAT_PROC_DWI_TO_DT_METADATA = Metadata(
    id="802161f8f0acfd7af6348446316cf5b2c086b7ef.boutiques",
    name="fat_proc_dwi_to_dt",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


FatProcDwiToDtParameters = typing.TypedDict('FatProcDwiToDtParameters', {
    "__STYX_TYPE__": typing.Literal["fat_proc_dwi_to_dt"],
    "in_dwi": InputPathType,
    "in_gradmat": InputPathType,
    "prefix": str,
    "in_bvals": typing.NotRequired[InputPathType | None],
    "mask": typing.NotRequired[InputPathType | None],
    "mask_from_struc": bool,
    "in_struc_res": typing.NotRequired[InputPathType | None],
    "in_ref_orig": typing.NotRequired[InputPathType | None],
    "prefix_dti": typing.NotRequired[str | None],
    "flip_x": bool,
    "flip_y": bool,
    "flip_z": bool,
    "no_flip": bool,
    "no_scale_out_1000": bool,
    "no_reweight": bool,
    "no_cumulative_wts": bool,
    "qc_fa_thr": typing.NotRequired[float | None],
    "qc_fa_max": typing.NotRequired[float | None],
    "qc_fa_unc_max": typing.NotRequired[float | None],
    "qc_v12_unc_max": typing.NotRequired[float | None],
    "qc_prefix": typing.NotRequired[str | None],
    "no_qc_view": bool,
    "no_cmd_out": bool,
    "workdir": typing.NotRequired[str | None],
    "no_clean": bool,
    "uncert_off": bool,
    "uncert_iters": typing.NotRequired[float | None],
    "uncert_extra_cmds": typing.NotRequired[str | None],
    "check_abs_min": typing.NotRequired[float | None],
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
        "fat_proc_dwi_to_dt": fat_proc_dwi_to_dt_cargs,
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
        "fat_proc_dwi_to_dt": fat_proc_dwi_to_dt_outputs,
    }.get(t)


class FatProcDwiToDtOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fat_proc_dwi_to_dt(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_files: OutputPathType
    """Output files generated with the specified prefix."""


def fat_proc_dwi_to_dt_params(
    in_dwi: InputPathType,
    in_gradmat: InputPathType,
    prefix: str,
    in_bvals: InputPathType | None = None,
    mask: InputPathType | None = None,
    mask_from_struc: bool = False,
    in_struc_res: InputPathType | None = None,
    in_ref_orig: InputPathType | None = None,
    prefix_dti: str | None = None,
    flip_x: bool = False,
    flip_y: bool = False,
    flip_z: bool = False,
    no_flip: bool = False,
    no_scale_out_1000: bool = False,
    no_reweight: bool = False,
    no_cumulative_wts: bool = False,
    qc_fa_thr: float | None = None,
    qc_fa_max: float | None = None,
    qc_fa_unc_max: float | None = None,
    qc_v12_unc_max: float | None = None,
    qc_prefix: str | None = None,
    no_qc_view: bool = False,
    no_cmd_out: bool = False,
    workdir: str | None = None,
    no_clean: bool = False,
    uncert_off: bool = False,
    uncert_iters: float | None = None,
    uncert_extra_cmds: str | None = None,
    check_abs_min: float | None = None,
) -> FatProcDwiToDtParameters:
    """
    Build parameters.
    
    Args:
        in_dwi: 4D volume of N DWIs. Required.
        in_gradmat: Input text file of N gradient vectors or bmatrices.
        prefix: Set prefix for output DWI data.
        in_bvals: Optional, if bvalue information is in a separate file from\
            the b-vectors or matrices.
        mask: Optional whole brain mask can be input; otherwise, automasking is\
            performed.
        mask_from_struc: Flag to make a mask using 3dSkullStrip+3dmask_tool\
            from the structural file.
        in_struc_res: Alignment of the output DWI to the REF data set via\
            anatomical reference; a version of the anatomical that has been\
            resampled to match the DWI set.
        in_ref_orig: Use another data set to adjust the DWI and subsequent\
            parameter dsets' orientation and origin.
        prefix_dti: Set prefix for output DTI data; default is 'dt'. Do not\
            include path information here.
        flip_x: Flip the DW gradients in the x-direction.
        flip_y: Flip the DW gradients in the y-direction.
        flip_z: Flip the DW gradients in the z-direction.
        no_flip: Do not flip the DW gradients.
        no_scale_out_1000: Turn off scaling of physical length units by 1000\
            for tensor fitting.
        no_reweight: Turn off reweighting and refitting of tensors during\
            estimation.
        no_cumulative_wts: Turn off displaying overall weight factors for each\
            gradient.
        qc_fa_thr: Set threshold for overlay FA volume in QC image.
        qc_fa_max: Set cbar max for overlay FA volume in QC image.
        qc_fa_unc_max: Set cbar max for overlay uncertainty (stdev) of FA in QC\
            image.
        qc_v12_unc_max: Set cbar max for overlay uncertainty (stdev) of V1\
            towards V2 direction for DTs in QC image.
        qc_prefix: Set the prefix of the QC image files separately.
        no_qc_view: Turn off generating QC image files.
        no_cmd_out: Don't save the command line call of this program and the\
            location where it was run.
        workdir: Specify a working directory, which can be removed.
        no_clean: Do not remove the working directory.
        uncert_off: Don't perform uncertainty calculation.
        uncert_iters: Set the number of Monte Carlo iterations for the\
            uncertainty calculation (default: 300).
        uncert_extra_cmds: Extra commands for the uncertainty calculations.
        check_abs_min: Help the program push through finding tiny negative\
            values in columns that should contain numbers >=0. Provide a tolerance\
            value VVV.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fat_proc_dwi_to_dt",
        "in_dwi": in_dwi,
        "in_gradmat": in_gradmat,
        "prefix": prefix,
        "mask_from_struc": mask_from_struc,
        "flip_x": flip_x,
        "flip_y": flip_y,
        "flip_z": flip_z,
        "no_flip": no_flip,
        "no_scale_out_1000": no_scale_out_1000,
        "no_reweight": no_reweight,
        "no_cumulative_wts": no_cumulative_wts,
        "no_qc_view": no_qc_view,
        "no_cmd_out": no_cmd_out,
        "no_clean": no_clean,
        "uncert_off": uncert_off,
    }
    if in_bvals is not None:
        params["in_bvals"] = in_bvals
    if mask is not None:
        params["mask"] = mask
    if in_struc_res is not None:
        params["in_struc_res"] = in_struc_res
    if in_ref_orig is not None:
        params["in_ref_orig"] = in_ref_orig
    if prefix_dti is not None:
        params["prefix_dti"] = prefix_dti
    if qc_fa_thr is not None:
        params["qc_fa_thr"] = qc_fa_thr
    if qc_fa_max is not None:
        params["qc_fa_max"] = qc_fa_max
    if qc_fa_unc_max is not None:
        params["qc_fa_unc_max"] = qc_fa_unc_max
    if qc_v12_unc_max is not None:
        params["qc_v12_unc_max"] = qc_v12_unc_max
    if qc_prefix is not None:
        params["qc_prefix"] = qc_prefix
    if workdir is not None:
        params["workdir"] = workdir
    if uncert_iters is not None:
        params["uncert_iters"] = uncert_iters
    if uncert_extra_cmds is not None:
        params["uncert_extra_cmds"] = uncert_extra_cmds
    if check_abs_min is not None:
        params["check_abs_min"] = check_abs_min
    return params


def fat_proc_dwi_to_dt_cargs(
    params: FatProcDwiToDtParameters,
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
    cargs.append("fat_proc_dwi_to_dt")
    cargs.append(execution.input_file(params.get("in_dwi")))
    cargs.extend([
        "-in_col_matA | -in_col_matT | -in_col_vec | -in_row_vec",
        execution.input_file(params.get("in_gradmat"))
    ])
    cargs.extend([
        "-prefix",
        params.get("prefix")
    ])
    if params.get("in_bvals") is not None:
        cargs.extend([
            "-in_bvals",
            execution.input_file(params.get("in_bvals"))
        ])
    if params.get("mask") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask"))
        ])
    if params.get("mask_from_struc"):
        cargs.append("-mask_from_struc")
    if params.get("in_struc_res") is not None:
        cargs.extend([
            "-in_struc_res",
            execution.input_file(params.get("in_struc_res"))
        ])
    if params.get("in_ref_orig") is not None:
        cargs.extend([
            "-in_ref_orig",
            execution.input_file(params.get("in_ref_orig"))
        ])
    if params.get("prefix_dti") is not None:
        cargs.extend([
            "-prefix_dti",
            params.get("prefix_dti")
        ])
    if params.get("flip_x"):
        cargs.append("-flip_x")
    if params.get("flip_y"):
        cargs.append("-flip_y")
    if params.get("flip_z"):
        cargs.append("-flip_z")
    if params.get("no_flip"):
        cargs.append("-no_flip")
    if params.get("no_scale_out_1000"):
        cargs.append("-no_scale_out_1000")
    if params.get("no_reweight"):
        cargs.append("-no_reweight")
    if params.get("no_cumulative_wts"):
        cargs.append("-no_cumulative_wts")
    if params.get("qc_fa_thr") is not None:
        cargs.extend([
            "-qc_fa_thr",
            str(params.get("qc_fa_thr"))
        ])
    if params.get("qc_fa_max") is not None:
        cargs.extend([
            "-qc_fa_max",
            str(params.get("qc_fa_max"))
        ])
    if params.get("qc_fa_unc_max") is not None:
        cargs.extend([
            "-qc_fa_unc_max",
            str(params.get("qc_fa_unc_max"))
        ])
    if params.get("qc_v12_unc_max") is not None:
        cargs.extend([
            "-qc_v12_unc_max",
            str(params.get("qc_v12_unc_max"))
        ])
    if params.get("qc_prefix") is not None:
        cargs.extend([
            "-qc_prefix",
            params.get("qc_prefix")
        ])
    if params.get("no_qc_view"):
        cargs.append("-no_qc_view")
    if params.get("no_cmd_out"):
        cargs.append("-no_cmd_out")
    if params.get("workdir") is not None:
        cargs.extend([
            "-workdir",
            params.get("workdir")
        ])
    if params.get("no_clean"):
        cargs.append("-no_clean")
    if params.get("uncert_off"):
        cargs.append("-uncert_off")
    if params.get("uncert_iters") is not None:
        cargs.extend([
            "-uncert_iters",
            str(params.get("uncert_iters"))
        ])
    if params.get("uncert_extra_cmds") is not None:
        cargs.extend([
            "-uncert_extra_cmds",
            params.get("uncert_extra_cmds")
        ])
    if params.get("check_abs_min") is not None:
        cargs.extend([
            "-check_abs_min",
            str(params.get("check_abs_min"))
        ])
    return cargs


def fat_proc_dwi_to_dt_outputs(
    params: FatProcDwiToDtParameters,
    execution: Execution,
) -> FatProcDwiToDtOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FatProcDwiToDtOutputs(
        root=execution.output_file("."),
        output_files=execution.output_file(params.get("prefix") + "*"),
    )
    return ret


def fat_proc_dwi_to_dt_execute(
    params: FatProcDwiToDtParameters,
    execution: Execution,
) -> FatProcDwiToDtOutputs:
    """
    This program fits tensors and DT parameters, as well as the uncertainty of DT
    parameters needed for tractography.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FatProcDwiToDtOutputs`).
    """
    params = execution.params(params)
    cargs = fat_proc_dwi_to_dt_cargs(params, execution)
    ret = fat_proc_dwi_to_dt_outputs(params, execution)
    execution.run(cargs)
    return ret


def fat_proc_dwi_to_dt(
    in_dwi: InputPathType,
    in_gradmat: InputPathType,
    prefix: str,
    in_bvals: InputPathType | None = None,
    mask: InputPathType | None = None,
    mask_from_struc: bool = False,
    in_struc_res: InputPathType | None = None,
    in_ref_orig: InputPathType | None = None,
    prefix_dti: str | None = None,
    flip_x: bool = False,
    flip_y: bool = False,
    flip_z: bool = False,
    no_flip: bool = False,
    no_scale_out_1000: bool = False,
    no_reweight: bool = False,
    no_cumulative_wts: bool = False,
    qc_fa_thr: float | None = None,
    qc_fa_max: float | None = None,
    qc_fa_unc_max: float | None = None,
    qc_v12_unc_max: float | None = None,
    qc_prefix: str | None = None,
    no_qc_view: bool = False,
    no_cmd_out: bool = False,
    workdir: str | None = None,
    no_clean: bool = False,
    uncert_off: bool = False,
    uncert_iters: float | None = None,
    uncert_extra_cmds: str | None = None,
    check_abs_min: float | None = None,
    runner: Runner | None = None,
) -> FatProcDwiToDtOutputs:
    """
    This program fits tensors and DT parameters, as well as the uncertainty of DT
    parameters needed for tractography.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        in_dwi: 4D volume of N DWIs. Required.
        in_gradmat: Input text file of N gradient vectors or bmatrices.
        prefix: Set prefix for output DWI data.
        in_bvals: Optional, if bvalue information is in a separate file from\
            the b-vectors or matrices.
        mask: Optional whole brain mask can be input; otherwise, automasking is\
            performed.
        mask_from_struc: Flag to make a mask using 3dSkullStrip+3dmask_tool\
            from the structural file.
        in_struc_res: Alignment of the output DWI to the REF data set via\
            anatomical reference; a version of the anatomical that has been\
            resampled to match the DWI set.
        in_ref_orig: Use another data set to adjust the DWI and subsequent\
            parameter dsets' orientation and origin.
        prefix_dti: Set prefix for output DTI data; default is 'dt'. Do not\
            include path information here.
        flip_x: Flip the DW gradients in the x-direction.
        flip_y: Flip the DW gradients in the y-direction.
        flip_z: Flip the DW gradients in the z-direction.
        no_flip: Do not flip the DW gradients.
        no_scale_out_1000: Turn off scaling of physical length units by 1000\
            for tensor fitting.
        no_reweight: Turn off reweighting and refitting of tensors during\
            estimation.
        no_cumulative_wts: Turn off displaying overall weight factors for each\
            gradient.
        qc_fa_thr: Set threshold for overlay FA volume in QC image.
        qc_fa_max: Set cbar max for overlay FA volume in QC image.
        qc_fa_unc_max: Set cbar max for overlay uncertainty (stdev) of FA in QC\
            image.
        qc_v12_unc_max: Set cbar max for overlay uncertainty (stdev) of V1\
            towards V2 direction for DTs in QC image.
        qc_prefix: Set the prefix of the QC image files separately.
        no_qc_view: Turn off generating QC image files.
        no_cmd_out: Don't save the command line call of this program and the\
            location where it was run.
        workdir: Specify a working directory, which can be removed.
        no_clean: Do not remove the working directory.
        uncert_off: Don't perform uncertainty calculation.
        uncert_iters: Set the number of Monte Carlo iterations for the\
            uncertainty calculation (default: 300).
        uncert_extra_cmds: Extra commands for the uncertainty calculations.
        check_abs_min: Help the program push through finding tiny negative\
            values in columns that should contain numbers >=0. Provide a tolerance\
            value VVV.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FatProcDwiToDtOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FAT_PROC_DWI_TO_DT_METADATA)
    params = fat_proc_dwi_to_dt_params(
        in_dwi=in_dwi,
        in_gradmat=in_gradmat,
        prefix=prefix,
        in_bvals=in_bvals,
        mask=mask,
        mask_from_struc=mask_from_struc,
        in_struc_res=in_struc_res,
        in_ref_orig=in_ref_orig,
        prefix_dti=prefix_dti,
        flip_x=flip_x,
        flip_y=flip_y,
        flip_z=flip_z,
        no_flip=no_flip,
        no_scale_out_1000=no_scale_out_1000,
        no_reweight=no_reweight,
        no_cumulative_wts=no_cumulative_wts,
        qc_fa_thr=qc_fa_thr,
        qc_fa_max=qc_fa_max,
        qc_fa_unc_max=qc_fa_unc_max,
        qc_v12_unc_max=qc_v12_unc_max,
        qc_prefix=qc_prefix,
        no_qc_view=no_qc_view,
        no_cmd_out=no_cmd_out,
        workdir=workdir,
        no_clean=no_clean,
        uncert_off=uncert_off,
        uncert_iters=uncert_iters,
        uncert_extra_cmds=uncert_extra_cmds,
        check_abs_min=check_abs_min,
    )
    return fat_proc_dwi_to_dt_execute(params, execution)


__all__ = [
    "FAT_PROC_DWI_TO_DT_METADATA",
    "FatProcDwiToDtOutputs",
    "FatProcDwiToDtParameters",
    "fat_proc_dwi_to_dt",
    "fat_proc_dwi_to_dt_params",
]
